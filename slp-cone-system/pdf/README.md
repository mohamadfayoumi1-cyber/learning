# PDF build

`../SLP_Cone_System_Design_Specification.pdf` is generated from these files. The HTML is
the source of truth for the document; edit it, then rebuild.

## Files

| File | Purpose |
|---|---|
| `body.html` | The document itself — Document Control, Parts I–III, Appendices A–C, all six figures as inline SVG |
| `cover.html` | Cover page |
| `style.css` | Shared print stylesheet (A4, page-break control, table and callout styling) |
| `toc.html` | **Generated** by `mktoc.py` — do not edit by hand |
| `build.mjs` | Renders the HTML to PDF with headless Chromium via Playwright, including running header and footer |
| `mktoc.py` | Builds `toc.html` from the page map |
| `merge.py` | Merges cover + contents + body, adds PDF bookmarks and metadata |
| `pipeline.sh` | Runs the whole sequence |

## Rebuild

```bash
ln -sfn "$(npm root -g)" node_modules   # once, so build.mjs can resolve playwright
bash pipeline.sh "$PWD"
```

## How the page numbers in the contents are produced

Chromium cannot tell you which page an element landed on, so the build does it in two
passes. Every `<h1 class="part">` and `<h2>` in `body.html` carries an invisible marker
span (`<span class="tocmk">QQnnnQQ</span>`, rendered white at 3 px). After the first
render, `pipeline.sh` extracts the text of each PDF page, finds which page each marker
landed on, and writes the real page numbers into `toc.html`. `merge.py` reuses the same
map to build the PDF bookmark tree.

The markers must stay in place — removing one breaks the contents page and the bookmarks
for that section.
