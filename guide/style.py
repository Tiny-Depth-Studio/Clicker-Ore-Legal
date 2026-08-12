"""Stylesheet for the generated guide pages, dark and light in one file."""

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
    --danger: #cf7a5a;
    --shadow: 0 8px 24px rgba(0,0,0,0.35);

    --cur-gold: #e0a752;
    --cur-diamond: #7fd1e0;
    --cur-essence: #b79ef0;
    --cur-taskium: #93a8d6;
    --cur-key: #d98a63;
    --cur-skillstone: #7fc9a0;
    --cur-orestone: #b5a68c;

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
    --danger: #a3492c;
    --shadow: 0 8px 20px rgba(90,70,30,0.12);
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
      --danger: #a3492c;
      --shadow: 0 8px 20px rgba(90,70,30,0.12);
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
    line-height: 1.65;
    -webkit-font-smoothing: antialiased;
  }

  ::selection { background: var(--accent); color: #14110d; }

  a { color: var(--accent-strong); text-decoration: none; }
  a:hover { text-decoration: underline; }
  a:focus-visible, button:focus-visible, summary:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }

  h1, h2, h3, h4 {
    font-family: var(--font-display);
    font-weight: 700;
    text-wrap: balance;
    letter-spacing: 0.01em;
    color: var(--text);
  }

  p { max-width: 68ch; }
  ul, ol { max-width: 68ch; }

  .shell {
    display: grid;
    grid-template-columns: 260px minmax(0, 1fr);
    min-height: 100vh;
  }

  .topbar {
    display: none;
    position: sticky;
    top: 0;
    z-index: 20;
    background: var(--bg-elevated);
    border-bottom: 1px solid var(--border);
    padding: 0.7rem 1rem;
    align-items: center;
    justify-content: space-between;
  }
  .topbar-title {
    font-family: var(--font-display);
    font-size: 0.95rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--accent-strong);
  }
  #nav-toggle { display: none; }
  .nav-toggle-btn {
    font-family: var(--font-display);
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.4rem 0.7rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.85rem;
  }

  nav.toc {
    position: sticky;
    top: 0;
    align-self: start;
    height: 100vh;
    overflow-y: auto;
    padding: 2rem 1.4rem 3rem;
    background: var(--bg-elevated);
    border-right: 1px solid var(--border);
  }
  .toc-home {
    display: inline-block;
    font-family: var(--font-display);
    font-size: 0.8rem;
    color: var(--text-dim);
    margin-bottom: 1.1rem;
  }
  .toc-home:hover { color: var(--accent-strong); text-decoration: none; }

  .toc-brand {
    font-family: var(--font-display);
    font-size: 1.05rem;
    letter-spacing: 0.03em;
    color: var(--accent-strong);
    margin-bottom: 0.15rem;
  }
  .toc-brand small {
    display: block;
    font-family: var(--font-body);
    font-style: italic;
    font-size: 0.78rem;
    color: var(--text-faint);
    letter-spacing: 0;
    margin-top: 0.25rem;
  }
  .toc-list {
    list-style: none;
    margin: 1.6rem 0 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
  }
  .toc-list a {
    display: block;
    color: var(--text-dim);
    font-size: 0.88rem;
    padding: 0.32rem 0.5rem;
    border-radius: 4px;
    border-left: 2px solid transparent;
  }
  .toc-list a:hover {
    color: var(--text);
    text-decoration: none;
    background: rgba(224,167,82,0.08);
    border-left-color: var(--accent);
  }
  .toc-num {
    font-family: var(--font-mono);
    color: var(--text-faint);
    font-size: 0.78rem;
    margin-right: 0.45rem;
  }

  main {
    padding: 3.2rem clamp(1.2rem, 4vw, 4rem) 6rem;
    max-width: 900px;
  }

  header.hero {
    margin-bottom: 3rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border);
  }
  .strata {
    height: 10px;
    width: 100%;
    border-radius: 3px;
    margin-bottom: 1.6rem;
    background: repeating-linear-gradient(
      90deg,
      var(--accent) 0 6%,
      var(--accent-2) 6% 11%,
      var(--border-soft) 11% 18%,
      var(--accent) 18% 24%,
      var(--border-soft) 24% 34%,
      var(--accent-2) 34% 40%,
      var(--accent) 40% 48%,
      var(--border-soft) 48% 58%,
      var(--accent-2) 58% 63%,
      var(--accent) 63% 72%,
      var(--border-soft) 72% 82%,
      var(--accent-2) 82% 90%,
      var(--accent) 90% 100%
    );
    opacity: 0.85;
  }
  .eyebrow {
    font-family: var(--font-display);
    text-transform: uppercase;
    letter-spacing: 0.14em;
    font-size: 0.72rem;
    color: var(--accent);
    margin-bottom: 0.6rem;
  }
  h1.title {
    font-size: clamp(2rem, 4.2vw, 2.9rem);
    margin: 0 0 0.7rem;
    line-height: 1.1;
  }
  .subtitle {
    color: var(--text-dim);
    font-size: 1.08rem;
    max-width: 62ch;
    margin: 0;
  }

  .langbar {
    margin: 1.8rem 0 0;
    padding-top: 1.2rem;
    border-top: 1px solid var(--border-soft);
  }
  .langbar-label {
    font-family: var(--font-display);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 0.68rem;
    color: var(--text-faint);
    margin-bottom: 0.55rem;
  }
  .langbar-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem 0.4rem;
  }
  .langbar-list a, .langbar-list span {
    font-family: var(--font-display);
    font-size: 0.78rem;
    padding: 0.18rem 0.55rem;
    border: 1px solid var(--border);
    border-radius: 20px;
    color: var(--text-dim);
    background: var(--bg-card);
  }
  .langbar-list a:hover {
    text-decoration: none;
    color: var(--text);
    border-color: var(--accent);
  }
  .langbar-list span {
    color: #14110d;
    background: var(--accent);
    border-color: var(--accent);
  }
  :root[data-theme="light"] .langbar-list span { color: #efe9da; }

  section {
    margin-bottom: 3.6rem;
    scroll-margin-top: 1.5rem;
  }
  .section-head {
    display: flex;
    align-items: baseline;
    gap: 0.7rem;
    margin-bottom: 0.3rem;
  }
  .section-num {
    font-family: var(--font-mono);
    color: var(--accent);
    font-size: 0.95rem;
  }
  h2 {
    font-size: 1.55rem;
    margin: 0;
  }
  .section-dek {
    color: var(--text-dim);
    font-size: 0.98rem;
    margin: 0.3rem 0 1.5rem;
    max-width: 62ch;
  }

  .callout {
    border-left: 3px solid var(--accent);
    background: var(--bg-card);
    padding: 0.95rem 1.2rem;
    border-radius: 0 6px 6px 0;
    margin: 1.2rem 0;
    font-size: 0.95rem;
  }
  .callout strong { color: var(--accent-strong); }
  .callout.warn { border-left-color: var(--danger); }
  .callout-label {
    font-family: var(--font-display);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.72rem;
    color: var(--accent);
    margin-bottom: 0.35rem;
  }
  .callout.warn .callout-label { color: var(--danger); }

  .currency-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 0.9rem;
    margin: 1.4rem 0;
  }
  .cur-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-top: 3px solid var(--dot);
    border-radius: 6px;
    padding: 0.95rem 1rem 1.05rem;
  }
  .cur-card h4 {
    margin: 0 0 0.5rem;
    font-size: 0.98rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .dot {
    width: 9px; height: 9px; border-radius: 50%;
    background: var(--dot);
    flex: none;
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--dot) 20%, transparent);
  }
  .cur-card p {
    margin: 0.15rem 0;
    font-size: 0.84rem;
    color: var(--text-dim);
    max-width: none;
  }
  .cur-card p b { color: var(--text); font-weight: 600; }

  .table-wrap {
    overflow-x: auto;
    margin: 1.2rem 0;
    border: 1px solid var(--border);
    border-radius: 8px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    min-width: 460px;
    font-size: 0.9rem;
  }
  thead th {
    text-align: left;
    font-family: var(--font-display);
    font-weight: 600;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    font-size: 0.72rem;
    color: var(--text-dim);
    background: var(--bg-elevated);
    padding: 0.6rem 0.85rem;
    border-bottom: 1px solid var(--border);
    white-space: nowrap;
  }
  tbody td {
    padding: 0.55rem 0.85rem;
    border-bottom: 1px solid var(--border-soft);
    font-variant-numeric: tabular-nums;
    color: var(--text);
  }
  tbody tr:last-child td { border-bottom: none; }
  tbody tr:nth-child(even) { background: color-mix(in srgb, var(--accent) 3%, transparent); }
  td.num, th.num { font-family: var(--font-mono); }
  td.strong { color: var(--accent-strong); font-weight: 600; }

  .strategy-track {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    margin: 1.4rem 0;
  }
  .strategy-stage {
    background: var(--bg-card);
    padding: 1rem 1.1rem;
  }
  .strategy-stage .stage-label {
    font-family: var(--font-display);
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--accent);
    margin-bottom: 0.4rem;
  }
  .strategy-stage ul {
    margin: 0;
    padding-left: 1.1rem;
    font-size: 0.86rem;
    color: var(--text-dim);
  }
  .strategy-stage li { margin-bottom: 0.25rem; }

  footer.doc-footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
    color: var(--text-faint);
    font-size: 0.8rem;
  }

  @media (max-width: 880px) {
    .shell { grid-template-columns: 1fr; }
    .topbar { display: flex; }
    nav.toc {
      position: fixed;
      inset: 0 20% 0 0;
      top: 52px;
      height: calc(100vh - 52px);
      transform: translateX(-100%);
      transition: transform 0.22s ease;
      z-index: 15;
      box-shadow: var(--shadow);
    }
    #nav-toggle:checked ~ .shell nav.toc {
      transform: translateX(0);
    }
    main { padding: 2rem 1.2rem 5rem; }
  }
"""
