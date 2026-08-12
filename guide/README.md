# Player guide build

`player_guide_<code>.html` in the repository root is **generated**. Edit the files in
this folder, then rebuild - never hand-edit the HTML, the next build overwrites it.

```bash
python guide/extract_names.py     # refresh in-game names from the Unity project
python guide/build.py             # write all 18 player_guide_*.html
python guide/build.py tr de       # or just some languages
```

## What lives where

| File | Holds |
| --- | --- |
| `numbers.py` | every balance number, verified against the game. One place to fix when balance changes. |
| `names.py` | **generated.** Skill, boss, pet, prestige, currency and store item names, per language, pulled from the game's own localization tables so the guide never invents a name the player does not see. |
| `extract_names.py` | the generator for `names.py`. Expects `Clicker-Ore-Game` next to this repository. |
| `lang/<code>.py` | the prose for one language: titles, paragraphs, bullets, callouts, table headers. |
| `render.py` | locale-aware number formatting, table generation, block rendering. |
| `style.py` | the stylesheet (dark and light). |
| `build.py` | page template and entry point. |

## Rules that keep the guide honest

- **Numbers never get typed into prose.** Language files use `{token}` placeholders that
  `numbers.py` fills, so a balance change is one edit plus a rebuild instead of 18 edits.
- **Names never get translated by hand.** They come from the game via `names.py`. If a name
  reads oddly, fix it in the game's localization table and re-run `extract_names.py`.
- **Number formatting follows the language.** Each `lang/<code>.py` declares a `locale`
  (`group` and `decimal`), so Turkish shows `100.000` and `0,5` while English shows
  `100,000` and `0.5`.
- **Store prices stay out.** Prices come from Steam at runtime in the player's own
  currency; the pack contents are listed, the price is not.
- **Spanish (Latin America) shares the European Spanish text** (`lang/es_la.py` copies
  `lang/es.py`), mirroring the game, which has no separate table for that locale either.

## Adding a language

1. Add the code to `LANGUAGES` in `build.py`.
2. Add its translation table name to `TABLES` in `extract_names.py` and re-run it.
3. Copy `lang/en.py` to `lang/<code>.py`, translate, and set `name`, `html_lang`, `locale`.
4. Run `python guide/build.py`, then add the new page to the language list in `index.html`.
