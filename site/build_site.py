"""Render index.html: a landing page for the game, fed by Steam.

Reads site/data/steam.json (written by site/steam.py) for the store copy, the
announcements and the artwork, and reads guide/lang/*.py for the language tiles,
so the home page never lists a guide by hand.

Images and the trailer thumbnail are hotlinked from Steam's CDN on purpose: they
carry a version stamp in the URL, so when the store art changes the next fetch
picks it up without any binary landing in this repository.

Also renders 404.html, which GitHub Pages serves for any missing path under
this site, so its links are absolute.

Run:  python site/steam.py && python site/build_site.py
"""

import datetime
import html
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "guide"))

import build as guide_build
import landing_style as style_module

DATA = os.path.join(HERE, "data", "steam.json")
OUT = os.path.join(ROOT, "index.html")
NOT_FOUND_OUT = os.path.join(ROOT, "404.html")

NEWS_SHOWN = 4
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

FLAG_DIR = os.path.join(ROOT, "assets", "flags")

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src 'self' https://shared.akamai.steamstatic.com https://cdn.akamai.steamstatic.com https://shared.fastly.steamstatic.com https://shared.cloudflare.steamstatic.com; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{name} - {tagline}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{description}">
<meta property="og:title" content="{name}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{header_image}">
<meta property="og:type" content="website">
<style>{css}</style>
</head>
<body>

<div class="topbar">
  <div class="topbar-inner">
    <a class="topbar-brand" href="#top">&#9935; {name}</a>
    <nav class="topbar-nav" aria-label="Sections">
      <a href="#news">Updates</a>
      <a href="#media">Screenshots</a>
      <a href="#guide">Guide</a>
      <a href="#legal">Legal</a>
    </nav>
    <a class="btn sm topbar-cta" href="{store_url}">Play free</a>
  </div>
</div>

<header class="hero" id="top">
  <div class="hero-bg" style="background-image:url('{header_image}')" role="presentation"></div>
  <div class="wrap">
    <a class="kicker studio-link" href="{studio_url}">{developer}</a>
    <h1>{name}</h1>
    <p class="lede">{description}</p>
    <div class="hero-actions">
      <a class="btn" href="{store_url}">Play free on Steam</a>
      <a class="btn ghost" href="#guide">Read the player guide</a>
    </div>
    <div class="chips">{chips}</div>
    <a class="hero-art" href="{store_url}" aria-label="{name} on Steam">
      <img src="{header_image}" alt="{name} store artwork" width="920" height="430">
    </a>
  </div>
</header>

<main>
  <section class="block" id="news">
    <div class="wrap">
      <div class="block-head">
        <span class="kicker">Updates</span>
        <h2>Fresh from the mine</h2>
        <p class="block-dek">Pulled from the Steam announcements - this page rebuilds itself when a new one goes up.</p>
      </div>
      <div class="news-grid">
{news}
      </div>
      <div class="block-more"><a class="btn ghost" href="{news_hub}">All announcements on Steam</a></div>
    </div>
  </section>

  <section class="block" id="media">
    <div class="wrap">
      <div class="block-head">
        <span class="kicker">Gallery</span>
        <h2>Down in the shaft</h2>
        <p class="block-dek">{media_dek}</p>
      </div>
      <div class="media-grid">
{media}
      </div>
    </div>
  </section>

  <section class="block" id="guide">
    <div class="wrap">
      <div class="block-head">
        <span class="kicker">{language_count} languages</span>
        <h2>Player guide</h2>
        <p class="block-dek">Pickaxes, skills, pets, golems, workers, enchantments, the character and equipment, the Arena, prestige, bosses and the store, explained in plain terms - the same guide in every language the game ships in. Pick yours:</p>
      </div>
      <div class="lang-grid">
{languages}
      </div>
    </div>
  </section>

  <section class="block" id="legal">
    <div class="wrap">
      <div class="block-head">
        <span class="kicker">Legal</span>
        <h2>The small print</h2>
        <p class="block-dek">What data the game collects, and the rules for using it.</p>
      </div>
      <div class="legal-row">
        <a class="btn ghost" href="privacy-policy.html">Privacy Policy</a>
        <a class="btn ghost" href="terms-of-service.html">Terms of Service</a>
      </div>
    </div>
  </section>
</main>

<div class="wrap">
  <footer class="site">
    <span>© {year} <a href="{studio_url}">{developer}</a> · <a href="mailto:{email}">{email}</a></span>
    <span>Updated {updated}</span>
  </footer>
</div>

</body>
</html>
"""

NOT_FOUND = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src 'self'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>Page not found - {name}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<style>{css}</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <span class="kicker">404</span>
    <h1>Nothing down here</h1>
    <p class="lede">This page does not exist. It may have moved, or the link was mistyped.</p>
    <div class="hero-actions">
      <a class="btn" href="{site_url}">Back to {name}</a>
      <a class="btn ghost" href="{site_url}#guide">Player guide</a>
    </div>
  </div>
</header>

<div class="wrap">
  <footer class="site">
    <span>© {year} <a href="{studio_url}">{developer}</a> · <a href="mailto:{email}">{email}</a></span>
  </footer>
</div>

</body>
</html>
"""

NEWS_CARD = """      <a class="news-card" href="{url}">
        <span class="news-meta"><span>{date}</span><span>{feedlabel}</span></span>
        <h3>{title}</h3>
        <p>{excerpt}</p>
        <span class="more">Read on Steam →</span>
      </a>"""

SHOT = """      <a class="shot{extra}" href="{href}">
        <img src="{src}" alt="{alt}" loading="lazy" width="600" height="338">
      </a>"""

LANG_CARD = """      <a class="lang-card" href="player_guide_{code}.html" hreflang="{html_lang}" lang="{html_lang}">
        <img class="lang-flag" src="assets/flags/{code}.png" alt="" width="40" height="40" loading="lazy">
        <span class="lang-text">
          <strong>{name}</strong>
          <span>{subtitle}</span>
        </span>
      </a>"""

EMAIL = "tinydepthstudio@gmail.com"
STUDIO_URL = "https://tiny-depth-studio.github.io/"
SITE_URL = "https://tiny-depth-studio.github.io/Clicker-Ore-Legal/"


def esc(text):
    return html.escape(text or "", quote=True)


def stamp(unix_seconds):
    moment = datetime.datetime.fromtimestamp(unix_seconds, datetime.timezone.utc)
    return "{0} {1} {2}".format(moment.day, MONTHS[moment.month - 1], moment.year)


def chips(app):
    values = []
    if app.get("is_free"):
        values.append(('<span class="chip free">Free to play</span>'))
    if app.get("release_date"):
        values.append('<span class="chip">Released {0}</span>'.format(esc(app["release_date"])))
    for platform in app.get("platforms", []):
        values.append('<span class="chip">{0}</span>'.format(esc(platform.title())))
    for genre in app.get("genres", [])[:4]:
        values.append('<span class="chip">{0}</span>'.format(esc(genre)))
    return "".join(values)


def news_cards(items):
    return "\n".join(
        NEWS_CARD.format(
            url=esc(item["url"]),
            date=stamp(item["date"]),
            feedlabel=esc(item.get("feedlabel") or "Steam"),
            title=esc(item["title"]),
            excerpt=esc(item["excerpt"]),
        )
        for item in items[:NEWS_SHOWN]
    )


def media_tiles(data):
    tiles = []
    trailer = data.get("trailer")
    if trailer:
        tiles.append(SHOT.format(
            extra=" trailer",
            href=esc(data["app"]["store_url"]),
            src=esc(trailer["thumb"]),
            alt=esc("{0} trailer".format(data["app"]["name"])),
        ))
    for index, shot in enumerate(data.get("screenshots", []), start=1):
        tiles.append(SHOT.format(
            extra="",
            href=esc(shot["full"]),
            src=esc(shot["thumb"]),
            alt=esc("{0} screenshot {1}".format(data["app"]["name"], index)),
        ))
    return "\n".join(tiles)


def language_cards():
    entries = []
    for code in guide_build.available_languages():
        if not os.path.exists(os.path.join(FLAG_DIR, code + ".png")):
            raise FileNotFoundError("missing flag image assets/flags/{0}.png".format(code))
        lang = guide_build.load_language(code)
        entries.append({
            "code": code,
            "html_lang": lang["html_lang"],
            "name": lang["name"],
            "subtitle": lang["brand_sub"],
        })
    entries.sort(key=lambda entry: entry["name"].casefold())
    return "\n".join(LANG_CARD.format(**entry) for entry in entries), len(entries)


def main():
    data = json.load(io.open(DATA, encoding="utf-8"))
    app = data["app"]
    languages, language_count = language_cards()
    newest = max((item["date"] for item in data["news"]), default=None)
    shots = len(data.get("screenshots", []))
    media_dek = "{0} shots from the mine{1}.".format(
        shots, ", plus the trailer" if data.get("trailer") else "")

    page = PAGE.format(
        css=style_module.CSS,
        name=esc(app["name"]),
        tagline="Idle mining and clicker game",
        description=esc(app["short_description"]),
        header_image=esc(app["header_image"]),
        store_url=esc(app["store_url"]),
        news_hub="https://steamcommunity.com/app/{0}/allnews/".format(app["id"]),
        developer=esc((app.get("developers") or ["Tiny Depth Studio"])[0]),
        chips=chips(app),
        news=news_cards(data["news"]),
        media=media_tiles(data),
        media_dek=esc(media_dek),
        languages=languages,
        language_count=language_count,
        year=datetime.datetime.fromtimestamp(newest, datetime.timezone.utc).year if newest else 2026,
        updated=stamp(newest) if newest else "",
        email=EMAIL,
        studio_url=STUDIO_URL,
    )
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    not_found = NOT_FOUND.format(
        css=style_module.CSS,
        name=esc(app["name"]),
        site_url=SITE_URL,
        developer=esc((app.get("developers") or ["Tiny Depth Studio"])[0]),
        year=datetime.datetime.fromtimestamp(newest, datetime.timezone.utc).year if newest else 2026,
        email=EMAIL,
        studio_url=STUDIO_URL,
    )
    io.open(NOT_FOUND_OUT, "w", encoding="utf-8", newline="\n").write(not_found)
    print("index.html: {0} news, {1} media tiles, {2} language tiles".format(
        min(NEWS_SHOWN, len(data["news"])), shots + (1 if data.get("trailer") else 0), language_count))


if __name__ == "__main__":
    main()
