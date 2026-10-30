# Landing page build

`index.html` in the repository root is **generated**. Edit the files here and rebuild;
never hand-edit the HTML, the next build overwrites it.

```bash
python site/steam.py        # fetch store data + announcements -> site/data/steam.json
python site/build_site.py   # render index.html
```

## What lives where

| File | Holds |
| --- | --- |
| `steam.py` | the only place that talks to Steam. Writes `data/steam.json`. |
| `data/steam.json` | **generated, committed.** Store copy, artwork URLs, the six newest announcements. Committed so a build works with no network. |
| `build_site.py` | renders `index.html` from that JSON plus the guide language modules, and `404.html`, which Pages serves for any missing path under the site. |
| `landing_style.py` | the landing page stylesheet. Named apart from `guide/style.py` so the two never shadow each other on `sys.path`. |

## Why the data is baked in

Neither `ISteamNews/GetNewsForApp` nor `store/api/appdetails` sends an
`Access-Control-Allow-Origin` header, so a static page cannot fetch them from the
browser - the request dies in CORS. Fetching at build time also means the page stays
up if Steam's API is briefly down, and there is no key or proxy to keep alive.

## How it stays current

`.github/workflows/steam-refresh.yml` runs twice a day (05:17 and 17:17 UTC), on every
push that touches `site/` or `guide/`, and on demand from the Actions tab
(`workflow_dispatch`). It fetches, rebuilds and commits **only when something actually
changed** - `steam.py` writes no fetch timestamp, so an unchanged feed produces an
unchanged file and no commit.

After a Steam announcement goes up, the page carries it at the next run at the latest.
To publish it immediately, trigger the workflow by hand or run the two commands above
and push.

## Security

The pages ship no JavaScript. Every page (landing, 404, guides, privacy policy and terms)
carries a Content-Security-Policy `<meta>`: no script, no forms, no `<base>`, images only
from this site (plus Steam's CDN on the landing page). `style-src` is `'unsafe-inline'`
because the pages use inline `<style>` blocks and a few `style="..."` attributes; with
scripts blocked that only allows CSS. The policy lives in the templates (`build_site.py`,
`guide/build.py`) and in the two hand-written legal pages.

Workflow actions are pinned to commit SHAs; Dependabot (`.github/dependabot.yml`)
proposes updates monthly.

## Notes

- **Announcements are shown as posted.** Steam's news API has no language parameter, so
  whatever language an announcement was written in is what appears. Only an excerpt is
  rendered (the body is Steam's own markup) with a link to the full post.
- **Duplicate announcements are folded.** The same title posted twice keeps the newest
  copy, which is why the feed shows six items where the API returns fourteen.
- **Artwork is hotlinked** from `shared.akamai.steamstatic.com`. Those URLs carry a
  version stamp, so a fetch picks up new store art without adding binaries here.
- The trailer is a thumbnail linking to the store page: Steam only serves DASH and HLS
  manifests for it, which a plain `<video>` tag cannot play.
- The app id lives in `steam.py` (`APP_ID = 3810540`).
