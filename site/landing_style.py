"""Stylesheet for the generated landing page.

Shares the palette and type scale with the player guide so the site reads as one
thing; the layout is its own, because a landing page and a long document want
different furniture.
"""

CSS = """
  :root {
    --bg: #14110d;
    --bg-elevated: #1d1811;
    --bg-card: #211b13;
    --text: #ede6d8;
    --text-dim: #a89a82;
    --text-faint: #766a55;
    --accent: #e0a752;
    --accent-strong: #f2bd6e;
    --accent-2: #7fb8ad;
    --border: #3a2f22;
    --border-soft: #2a2318;
    --shadow: 0 10px 30px rgba(0,0,0,0.4);

    --font-display: "Bahnschrift", "Segoe UI Semibold", "Arial Narrow Bold", "Arial Narrow", sans-serif;
    --font-body: "Sitka Text", "Iowan Old Style", Georgia, "Times New Roman", serif;
    --font-mono: "Cascadia Mono", "Consolas", "SF Mono", ui-monospace, monospace;
  }

  :root[data-theme="light"] {
    --bg: #efe9da;
    --bg-elevated: #e6ddc8;
    --bg-card: #f3ede0;
    --text: #241d14;
    --text-dim: #5c5138;
    --text-faint: #857656;
    --accent: #a8621a;
    --accent-strong: #8a4e12;
    --accent-2: #2f7a70;
    --border: #d3c5a4;
    --border-soft: #ddd0b1;
    --shadow: 0 10px 26px rgba(90,70,30,0.14);
  }

  @media (prefers-color-scheme: light) {
    :root:not([data-theme="dark"]) {
      --bg: #efe9da;
      --bg-elevated: #e6ddc8;
      --bg-card: #f3ede0;
      --text: #241d14;
      --text-dim: #5c5138;
      --text-faint: #857656;
      --accent: #a8621a;
      --accent-strong: #8a4e12;
      --accent-2: #2f7a70;
      --border: #d3c5a4;
      --border-soft: #ddd0b1;
      --shadow: 0 10px 26px rgba(90,70,30,0.14);
    }
  }

  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-body);
    font-size: 17px;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }
  img { max-width: 100%; display: block; }
  a { color: var(--accent-strong); text-decoration: none; }
  a:hover { text-decoration: underline; }
  a:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
    border-radius: 4px;
  }
  h1, h2, h3 {
    font-family: var(--font-display);
    font-weight: 700;
    letter-spacing: 0.01em;
    text-wrap: balance;
    margin: 0;
  }

  .topbar {
    position: sticky;
    top: 0;
    z-index: 20;
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
    padding: 0.6rem clamp(1rem, 4vw, 2.4rem);
    background: color-mix(in srgb, var(--bg-elevated) 92%, transparent);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(8px);
  }
  .topbar-brand {
    font-family: var(--font-display);
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-size: 0.9rem;
    color: var(--accent-strong);
    margin-right: auto;
  }
  .topbar-nav {
    display: flex;
    gap: 0.2rem 0.9rem;
    flex-wrap: wrap;
    font-family: var(--font-display);
    font-size: 0.82rem;
  }
  .topbar-nav a { color: var(--text-dim); }
  .topbar-nav a:hover { color: var(--text); text-decoration: none; }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-family: var(--font-display);
    font-size: 0.86rem;
    padding: 0.45rem 0.95rem;
    border-radius: 6px;
    border: 1px solid var(--accent);
    background: var(--accent);
    color: #14110d;
    white-space: nowrap;
  }
  .btn:hover { background: var(--accent-strong); border-color: var(--accent-strong); text-decoration: none; }
  :root[data-theme="light"] .btn { color: #f7f2e6; }
  .btn.ghost {
    background: transparent;
    color: var(--text);
    border-color: var(--border);
  }
  .btn.ghost:hover { border-color: var(--accent); background: color-mix(in srgb, var(--accent) 8%, transparent); }

  .wrap {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 clamp(1rem, 4vw, 2.4rem);
  }

  .strata {
    height: 10px;
    border-radius: 3px;
    margin: 1.8rem 0 1.6rem;
    background: repeating-linear-gradient(
      90deg,
      var(--accent) 0 6%, var(--accent-2) 6% 11%, var(--border-soft) 11% 18%,
      var(--accent) 18% 24%, var(--border-soft) 24% 34%, var(--accent-2) 34% 40%,
      var(--accent) 40% 48%, var(--border-soft) 48% 58%, var(--accent-2) 58% 63%,
      var(--accent) 63% 72%, var(--border-soft) 72% 82%, var(--accent-2) 82% 90%,
      var(--accent) 90% 100%
    );
    opacity: 0.85;
  }

  .hero {
    display: grid;
    grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
    gap: clamp(1.4rem, 4vw, 3rem);
    align-items: center;
    padding-bottom: 3rem;
    border-bottom: 1px solid var(--border);
  }
  .eyebrow {
    font-family: var(--font-display);
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.72rem;
    color: var(--accent);
    margin-bottom: 0.7rem;
  }
  .hero h1 {
    font-size: clamp(2.2rem, 6vw, 3.2rem);
    line-height: 1.05;
    margin-bottom: 0.8rem;
  }
  .hero p.lede {
    color: var(--text-dim);
    font-size: 1.06rem;
    max-width: 46ch;
    margin: 0 0 1.3rem;
  }
  .chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem 0.4rem;
    margin-bottom: 1.5rem;
  }
  .chip {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    padding: 0.2rem 0.5rem;
    border: 1px solid var(--border);
    border-radius: 20px;
    color: var(--text-dim);
    background: var(--bg-card);
  }
  .chip.free { color: var(--accent); border-color: color-mix(in srgb, var(--accent) 40%, var(--border)); }
  .hero-actions { display: flex; flex-wrap: wrap; gap: 0.6rem; }
  .hero-art {
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    box-shadow: var(--shadow);
  }

  section.block { padding: 3rem 0; border-bottom: 1px solid var(--border); }
  section.block:last-of-type { border-bottom: none; }
  .block-head {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
    margin-bottom: 0.3rem;
  }
  .block-head h2 { font-size: 1.5rem; }
  .block-head a { font-family: var(--font-display); font-size: 0.84rem; }
  .block-dek {
    color: var(--text-dim);
    font-size: 0.96rem;
    margin: 0 0 1.6rem;
    max-width: 60ch;
  }

  .news-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 0.9rem;
  }
  .news-card {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.15rem;
    color: inherit;
  }
  .news-card:hover {
    text-decoration: none;
    border-left-color: var(--accent-strong);
    background: color-mix(in srgb, var(--accent) 6%, var(--bg-card));
  }
  .news-meta {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: var(--text-faint);
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
  }
  .news-card h3 { font-size: 1.02rem; line-height: 1.3; color: var(--text); }
  .news-card p { margin: 0; font-size: 0.88rem; color: var(--text-dim); }
  .news-card .more { font-family: var(--font-display); font-size: 0.8rem; color: var(--accent-strong); margin-top: auto; }

  .media-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 0.7rem;
  }
  .shot {
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    background: var(--bg-card);
    position: relative;
  }
  .shot img { transition: transform 0.25s ease; aspect-ratio: 16 / 9; object-fit: cover; }
  .shot:hover img { transform: scale(1.03); }
  .shot.trailer::after {
    content: "▶";
    position: absolute;
    inset: 0;
    display: grid;
    place-items: center;
    font-size: 2rem;
    color: #f7f2e6;
    background: rgba(20,17,13,0.35);
  }

  .lang-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(196px, 1fr));
    gap: 0.6rem;
  }
  .lang-card {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.72rem 0.85rem;
    transition: border-color 0.15s ease, background 0.15s ease, transform 0.15s ease;
  }
  .lang-card:hover {
    text-decoration: none;
    border-color: var(--accent);
    background: color-mix(in srgb, var(--accent) 6%, var(--bg-card));
    transform: translateY(-1px);
  }
  .lang-code {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.04em;
    color: var(--accent);
    background: color-mix(in srgb, var(--accent) 12%, transparent);
    border: 1px solid color-mix(in srgb, var(--accent) 30%, var(--border));
    border-radius: 5px;
    padding: 0.22rem 0.4rem;
    flex: none;
    min-width: 3.4rem;
    text-align: center;
  }
  .lang-text { display: flex; flex-direction: column; min-width: 0; }
  .lang-text strong { font-family: var(--font-display); font-size: 0.95rem; font-weight: 600; color: var(--text); line-height: 1.25; }
  .lang-text span { font-size: 0.78rem; color: var(--text-dim); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

  .legal-row { display: flex; flex-wrap: wrap; gap: 0.6rem; }
  .legal-row a {
    font-family: var(--font-display);
    font-size: 0.86rem;
    padding: 0.5rem 0.9rem;
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent-2);
    border-radius: 0 8px 8px 0;
    background: var(--bg-card);
    color: var(--text);
  }
  .legal-row a:hover { text-decoration: none; background: color-mix(in srgb, var(--accent-2) 8%, var(--bg-card)); }

  footer.site {
    padding: 2rem 0 3rem;
    color: var(--text-faint);
    font-size: 0.82rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem 1.2rem;
    justify-content: space-between;
    border-top: 1px solid var(--border);
  }
  footer.site a { color: var(--text-dim); text-decoration: underline; text-underline-offset: 2px; }

  @media (max-width: 820px) {
    .hero { grid-template-columns: 1fr; padding-bottom: 2.2rem; }
    .hero-art { order: -1; }
    .topbar-nav { display: none; }
  }
"""
