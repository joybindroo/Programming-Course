# Agents Guide

This repository powers the "Programming Course" GitHub Pages site (`https://joybindroo.github.io/Programming-Course/`). Each module lives in Markdown under the project root and is mirrored to a static HTML page so the site loads without client-side rendering.

## Repo Layout
- `Module*-*.md` – source-of-truth notes for every module.
- `Module*-*.html` – generated static pages published via GitHub Pages.
- `index.html` – landing page that links to every module guide.
- `README.md` – Markdown syllabus and overview.
- `scripts/generate_module_pages.py` – helper script that converts Markdown to HTML using consistent styling.

### Current Module Map
1. Module 1 – Foundations of Computer Science
2. Module 2 – Programming Fundamentals
3. Module 3 – Object-Oriented Programming
4. Module 4 – Data Structures & Algorithms
5. Module 5 – Advanced Topics
6. Module 6 – Software Delivery & DevOps
7. Module 7 – Docker Mastery
8. Module 8 – Database Programming & Tooling

## Editing Existing Modules
1. Open the relevant `ModuleX-Name.md` file.
2. Maintain Markdown structure (`#` for module title, `##` for major sections, `###`/`####` as needed).
3. Keep nested lists indented with four spaces so the Python Markdown renderer preserves hierarchy.
4. Favor concise explanations followed by concrete exercises, code, or tables.
5. Save the file in UTF-8 ASCII text only (no smart quotes) unless the module already contains unicode symbols.
6. After editing, regenerate the HTML (see "Converting Markdown to HTML").

### Adding Hyperlinks Inside Modules
- Use inline Markdown links (`[label](relative-or-absolute-url)`), keeping URLs relative when linking to repo assets (e.g., `[Module 2](./Module2-Programming-Fundamentals.md)`).
- For external links, include the full `https://` URL and keep descriptive labels (avoid "click here").
- If linking between generated HTML pages, prefer the Markdown source links and rely on the build script; it rewrites nothing but the HTML will contain the same relative paths.

## Converting Markdown to HTML
The repo ships with a Python helper so you never edit the HTML by hand.

1. Ensure Python 3.11+ is available.
2. Install the Markdown package once (either globally or in a venv):
   ```bash
   python3 -m pip install markdown
   ```
   or
   ```bash
   python3 -m venv .venv
   . .venv/bin/activate
   pip install markdown
   ```
3. Run the generator from the repo root:
   ```bash
   python scripts/generate_module_pages.py
   ```
4. The script scans every `Module*.md` (excluding `*-orig.md` backups) and rewrites the matching `.html` files with consistent styling.
5. Re-run the script whenever you change Markdown or add a new module so GitHub Pages always has the up-to-date HTML artifacts.

## Adding Hyperlinks on the Landing Page
1. Edit `index.html` and update the Module card list as needed.
2. Use the pattern `<a class="module-link" href="ModuleX-Name.html">View module guide</a>` to target the generated HTML.
3. If you add new CTAs or reference links, keep styling consistent with existing classes (`btn primary`, `btn secondary`).

## Adding a New Module
1. **Create Markdown**
   - Copy the naming pattern `Module6-Topic.md`.
   - Start with a level-1 heading (`# Module 6: Topic Name`).
   - Include an opening blurb plus structured sections, exercises, and takeaway lists.
2. **Update the Syllabus**
   - In `README.md`, add a new module section with a Markdown link to the file and bullet summaries.
3. **Update the Landing Page**
   - In `index.html`, duplicate an existing `.module-card`, adjust the label (`Module 6`), title, blurb, bullet list, and hyperlink to the future HTML (`Module6-Topic.html`).
4. **Generate HTML**
   - Run `python scripts/generate_module_pages.py` to create `Module6-Topic.html` so GitHub Pages can serve it.
5. **Cross-Link (Optional)**
   - If earlier modules reference this new content, add Markdown links in those files.
6. **Verify**
   - Open the updated HTML in a browser (double-click locally or use a static server) to ensure layout and content render correctly.

## Contribution Checklist for Agents
- [ ] Edit or add Markdown content.
- [ ] Run the generator script to refresh HTML.
- [ ] Update `README.md` and `index.html` whenever new modules or summaries change.
- [ ] Spot-check rendering (desktop + mobile widths) before handing work back.
- [ ] Leave HTML artifacts staged for commit so the static site stays in sync.

Following these steps keeps Markdown as the single source of truth while guaranteeing the GitHub Pages site reflects every change.
