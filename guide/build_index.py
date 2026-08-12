"""Regenerate the language grid inside index.html from the lang/ modules.

The home page used to hand-list the guides, which is how it ended up looking as
if only English and Turkish existed. Now every language gets an identical tile
and the block is generated, so adding a language is one file plus a rebuild.

The tiles carry each language's own name and its own word for "player guide",
taken from lang/<code>.py, so a visitor recognises their language without
reading English first.

Run:  python guide/build_index.py
"""

import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import build as build_module

START = "      <!-- guide-links:start -->"
END = "      <!-- guide-links:end -->"

CARD = """      <a class="lang-card" href="player_guide_{code}.html" hreflang="{html_lang}" lang="{html_lang}">
        <span class="lang-code">{badge}</span>
        <span class="lang-text">
          <strong>{name}</strong>
          <span>{subtitle}</span>
        </span>
      </a>"""

BADGES = {
    "en": "EN", "tr": "TR", "de": "DE", "fr": "FR", "es": "ES", "es_la": "ES-419",
    "it": "IT", "pl": "PL", "pt_br": "PT-BR", "ru": "RU", "uk": "UK", "ja": "JA",
    "ko": "KO", "zh_hans": "ZH-CN", "zh_hant": "ZH-TW", "th": "TH", "id": "ID", "vi": "VI",
}


def cards():
    entries = []
    for code in build_module.available_languages():
        lang = build_module.load_language(code)
        entries.append({
            "code": code,
            "html_lang": lang["html_lang"],
            "name": lang["name"],
            "subtitle": lang["brand_sub"],
            "badge": BADGES.get(code, code.upper()),
        })
    entries.sort(key=lambda entry: entry["name"].casefold())
    return [CARD.format(**entry) for entry in entries]


def main():
    path = os.path.join(ROOT, "index.html")
    source = io.open(path, encoding="utf-8").read()
    if START not in source or END not in source:
        raise SystemExit("index.html is missing the guide-links markers")
    head, rest = source.split(START, 1)
    _, tail = rest.split(END, 1)
    block = "\n".join(cards())
    io.open(path, "w", encoding="utf-8", newline="\n").write(
        head + START + "\n" + block + "\n" + END + tail)
    print("index.html: {0} language tiles".format(len(cards())))


if __name__ == "__main__":
    main()
