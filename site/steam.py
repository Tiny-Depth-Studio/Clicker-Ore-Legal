"""Pull the store data and announcements for the game off Steam.

Steam's two endpoints send no CORS header, so the page cannot fetch them from
the browser - the data has to be baked in at build time. This script fetches it
and writes site/data/steam.json, which build_site.py renders and which is
committed so a build works without network access.

Deliberately no fetch timestamp in the output: the scheduled workflow commits
only when the file actually changes, and a timestamp would make every run look
like a change.

Run:  python site/steam.py
"""

import datetime
import html
import io
import json
import os
import re
import sys
import urllib.request

APP_ID = 3810540
STORE_URL = "https://store.steampowered.com/app/{0}/".format(APP_ID)
NEWS_URL = ("https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
            "?appid={0}&count=30&maxlength=0".format(APP_ID))
DETAILS_URL = ("https://store.steampowered.com/api/appdetails"
               "?appids={0}&l=english&cc=us".format(APP_ID))

DATE_FORMATS = ["%d %b, %Y", "%b %d, %Y", "%d %B %Y", "%B %d, %Y", "%d %b %Y"]

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "steam.json")

NEWS_KEPT = 6
EXCERPT_CHARS = 220


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "clicker-ore-site/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def plain_text(markup):
    text = re.sub(r"<br\s*/?>", " ", markup, flags=re.I)
    text = re.sub(r"</(p|div|h\d|li)>", " ", text, flags=re.I)
    text = re.sub(r"\[/?[^\]]{1,40}\]", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def excerpt(contents, title):
    text = plain_text(contents)
    if text.lower().startswith(title.lower()):
        text = text[len(title):].lstrip(" -:—")
    if len(text) <= EXCERPT_CHARS:
        return text
    cut = text[:EXCERPT_CHARS]
    space = cut.rfind(" ")
    return (cut[:space] if space > EXCERPT_CHARS * 0.6 else cut).rstrip(" ,;:-") + "…"


def collect_news():
    payload = fetch(NEWS_URL)
    items = payload.get("appnews", {}).get("newsitems", [])
    items.sort(key=lambda item: item.get("date", 0), reverse=True)
    best = {}
    for item in items:
        key = re.sub(r"\s+", " ", item.get("title", "")).strip().casefold()
        if key and key not in best:
            best[key] = item
    kept = sorted(best.values(), key=lambda item: item.get("date", 0), reverse=True)[:NEWS_KEPT]
    return [
        {
            "gid": item.get("gid"),
            "title": item.get("title", "").strip(),
            "url": item.get("url"),
            "date": item.get("date"),
            "feedlabel": item.get("feedlabel"),
            "excerpt": excerpt(item.get("contents", ""), item.get("title", "")),
        }
        for item in kept
    ]


def release_date(raw):
    """Steam formats this string per requesting region, so pin it to one shape.

    The scheduled run on a US-hosted runner returned "Jul 26, 2026" where a
    Turkish machine got "26 Jul, 2026" for the same app. Left alone the two
    builds would keep overwriting each other and every run would commit.
    """
    text = (raw or "").strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.datetime.strptime(text, fmt).strftime("%d %b %Y").lstrip("0")
        except ValueError:
            continue
    return text


def collect_app():
    payload = fetch(DETAILS_URL)
    entry = payload.get(str(APP_ID), {})
    if not entry.get("success"):
        raise SystemExit("Steam returned no store data for app {0}".format(APP_ID))
    data = entry["data"]
    movies = data.get("movies") or []
    return {
        "app": {
            "id": APP_ID,
            "name": data.get("name"),
            "store_url": STORE_URL,
            "short_description": plain_text(data.get("short_description", "")),
            "header_image": data.get("header_image"),
            "capsule_image": data.get("capsule_image"),
            "is_free": bool(data.get("is_free")),
            "release_date": release_date((data.get("release_date") or {}).get("date")),
            "developers": data.get("developers") or [],
            "genres": [genre["description"] for genre in data.get("genres") or []],
            "platforms": [name for name, on in (data.get("platforms") or {}).items() if on],
        },
        "screenshots": [
            {"thumb": shot["path_thumbnail"], "full": shot["path_full"]}
            for shot in data.get("screenshots") or []
        ],
        "trailer": ({"thumb": movies[0]["thumbnail"], "name": movies[0].get("name")}
                    if movies else None),
    }


def main():
    payload = collect_app()
    payload["news"] = collect_news()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    text = json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    previous = io.open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(text)
    print("{0}: {1} news, {2} screenshots{3}".format(
        os.path.relpath(OUT, os.path.dirname(HERE)),
        len(payload["news"]),
        len(payload["screenshots"]),
        "" if text != previous else " (unchanged)"))


if __name__ == "__main__":
    sys.exit(main())
