"""Build static HTML pages for each module Markdown file."""

from __future__ import annotations

import html
import re
from pathlib import Path

import markdown


MODULE_TEMPLATE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>%%MODULE_TITLE%% | Programming Course</title>
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
    <link href=\"https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap\" rel=\"stylesheet\">
    <style>
        :root {
            --bg: #060b1b;
            --panel: #0f1731;
            --card: rgba(18, 27, 56, 0.9);
            --accent: #f6a227;
            --accent-strong: #f15c2c;
            --text: #f0f3ff;
            --muted: #aab5d6;
            --outline: rgba(255, 255, 255, 0.08);
            --code-bg: #0c1127;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: 'Space Grotesk', 'Segoe UI', sans-serif;
            background: radial-gradient(circle at top, #0c1440, var(--bg));
            color: var(--text);
            min-height: 100vh;
            line-height: 1.7;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            background: radial-gradient(circle at 20% 15%, rgba(246, 162, 39, 0.2), transparent 45%),
                        radial-gradient(circle at 80% -10%, rgba(126, 220, 226, 0.18), transparent 50%);
            pointer-events: none;
            z-index: -1;
        }

        main {
            width: min(960px, 92vw);
            margin: 0 auto;
            padding-bottom: 6rem;
        }

        .top-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1.5rem 0 0;
            width: min(960px, 92vw);
            margin: 0 auto;
        }

        .back-link {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            color: var(--muted);
            text-decoration: none;
            font-size: 0.95rem;
        }

        .back-link:hover {
            color: var(--accent);
        }

        header.hero {
            padding: 3rem 0 2rem;
        }

        .eyebrow {
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--accent);
            font-size: 0.8rem;
        }

        h1 {
            font-size: clamp(2.2rem, 5vw, 3.2rem);
            margin: 0.8rem 0 1rem;
        }

        .hero p.hero-copy {
            color: var(--muted);
            max-width: 640px;
        }

        .hero-actions {
            margin-top: 1.6rem;
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 0.85rem 1.6rem;
            border-radius: 999px;
            border: 1px solid var(--outline);
            color: var(--text);
            text-decoration: none;
            font-weight: 600;
            transition: border-color 150ms ease, color 150ms ease;
        }

        .btn:hover {
            border-color: var(--accent);
            color: var(--accent);
        }

        .module-shell {
            background: var(--card);
            border-radius: 28px;
            padding: 2.25rem;
            border: 1px solid var(--outline);
            box-shadow: 0 35px 60px rgba(0, 0, 0, 0.45);
        }

        .module-shell h1 {
            font-size: 2rem;
            margin-top: 0;
        }

        .module-shell h2 {
            margin-top: 2.5rem;
        }

        .module-shell h3,
        .module-shell h4,
        .module-shell h5 {
            margin-top: 2rem;
        }

        .module-shell p,
        .module-shell li {
            color: var(--muted);
        }

        .module-shell ul,
        .module-shell ol {
            padding-left: 1.4rem;
        }

        .module-shell code {
            background: rgba(255, 255, 255, 0.08);
            padding: 0.1rem 0.35rem;
            border-radius: 6px;
            font-size: 0.95rem;
        }

        pre code {
            display: block;
            background: var(--code-bg);
            padding: 1rem;
            border-radius: 12px;
            overflow-x: auto;
            line-height: 1.5;
        }

        .status {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.9rem;
            color: var(--muted);
        }

        .status-dot {
            width: 0.55rem;
            height: 0.55rem;
            border-radius: 50%;
            background: var(--accent);
            animation: pulse 2.4s ease-in-out infinite;
        }

        @keyframes pulse {
            0% { opacity: 0.3; transform: scale(0.8); }
            50% { opacity: 1; transform: scale(1); }
            100% { opacity: 0.3; transform: scale(0.8); }
        }

        footer {
            text-align: center;
            color: var(--muted);
            padding: 3rem 0;
            font-size: 0.95rem;
        }

        @media (max-width: 640px) {
            .module-shell {
                padding: 1.5rem;
            }

            .top-bar {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }
        }
    </style>
</head>
<body>
    <div class=\"top-bar\">
        <a class=\"back-link\" href=\"index.html\">⬅ Back to overview</a>
        <span class=\"status\"><span class=\"status-dot\"></span>Live module notes</span>
    </div>

    <main>
        <header class=\"hero\">
            <p class=\"eyebrow\">%%MODULE_LABEL%%</p>
            <h1>%%MODULE_TITLE%%</h1>
            <p class=\"hero-copy\">%%MODULE_SUBTITLE%%</p>
            <div class=\"hero-actions\">
                <a class=\"btn\" href=\"%%MARKDOWN_FILE%%\" download>Download Markdown</a>
                <a class=\"btn\" href=\"README.md\">Full Course Index</a>
            </div>
        </header>

        <article class=\"module-shell\">
            %%MODULE_CONTENT%%
        </article>
    </main>

    <footer>
        Need edits? Update the Markdown file and rebuild this page.
    </footer>
</body>
</html>
"""


LIST_ITEM = re.compile(r'(?:[-+*]|\d+\.)\s+')


def ensure_list_separation(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    fixed: list[str] = []

    for line in lines:
        stripped = line.lstrip()
        is_list_line = bool(LIST_ITEM.match(stripped))
        prev_line = fixed[-1] if fixed else ""
        prev_is_blank = not prev_line.strip()
        prev_is_list = bool(LIST_ITEM.match(prev_line.lstrip()))

        if is_list_line and not prev_is_blank and not prev_is_list:
            fixed.append("")

        fixed.append(line)

    return "\n".join(fixed)


def build_pages() -> None:
    extensions = [
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',
        'markdown.extensions.sane_lists',
    ]

    root = Path('.')
    module_files = sorted(root.glob('Module*.md'))
    module_files = [p for p in module_files if '-orig' not in p.stem]

    for md_path in module_files:
        raw_text = md_path.read_text(encoding='utf-8').strip()
        h1 = re.search(r'^#\s+(.+)', raw_text, re.MULTILINE)
        h2 = re.search(r'^##\s+(.+)', raw_text, re.MULTILINE)

        module_title = h1.group(1).strip() if h1 else md_path.stem.replace('-', ' ')
        module_subtitle = h2.group(1).strip() if h2 else f"Direct notes sourced from {md_path.name}"

        label_part = md_path.stem.split('-')[0]
        match = re.match(r'(Module)(\d+)', label_part)
        if match:
            module_label = f"{match.group(1)} {match.group(2)}"
        else:
            module_label = label_part.replace('-', ' ')

        body_md = raw_text
        if h1:
            start, end = h1.span()
            body_md = raw_text[:start] + raw_text[end:]
        body_md = ensure_list_separation(body_md.lstrip('\n'))
        if not body_md.strip():
            body_md = raw_text

        module_html = markdown.markdown(body_md, extensions=extensions, output_format='html5')

        replacements = {
            'MODULE_LABEL': html.escape(module_label),
            'MODULE_TITLE': html.escape(module_title),
            'MODULE_SUBTITLE': html.escape(module_subtitle),
            'MARKDOWN_FILE': md_path.name,
            'MODULE_CONTENT': module_html,
        }

        page = MODULE_TEMPLATE
        for key, value in replacements.items():
            page = page.replace(f"%%{key}%%", value)

        output_path = md_path.with_suffix('.html')
        output_path.write_text(page, encoding='utf-8')
        print(f"Generated {output_path.relative_to(root)}")


if __name__ == '__main__':
    build_pages()
