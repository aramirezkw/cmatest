# KWIQ Agentic Overlay

An interactive prototype of the KWIQ AI surface for KW Command — a warm-concierge AI
copilot with a guided **CMA (Comparative Market Analysis)** flow. Built on the XDS
design system. No framework, no build step — the entire prototype (HTML, JS, fonts,
and assets) is bundled into a single self-contained file.

## View it

- **Locally:** open `index.html` in a modern browser, or serve the folder:
  ```bash
  python3 -m http.server 8899
  # then open http://localhost:8899/
  ```
- **GitHub Pages:** enable Pages on the `main` branch (root). The site loads `index.html`.

> A current browser is required — assets are decompressed at load time via
> `DecompressionStream` (supported in all up-to-date browsers).

## What's in here

| File | Purpose |
|---|---|
| `index.html` | The runnable prototype (GitHub Pages entry point) |
| `agenticoverlay.html` | Identical bundle, original filename |
| `_template_src.html` | Editable source — the readable HTML/JS that gets bundled |
| `_rebuild.py` | Re-bundles `_template_src.html` back into the `.html` files |

## Highlights

- **Concierge AI surface** — time-of-day greeting, prompt chips, staggered entrance
  animation, and a soft open chime.
- **Guided CMA flow** — *ask → confirm → draft → present*: clarifying questions
  (comps, status, neighborhoods, beds/baths), a confirmation summary, a cycling-message
  loading treatment, and a premium HouseCanary-style report (estimated value with a
  range bar, subject specs, market KPIs, a price-positioning chart, and adjusted
  comparable-sales cards). If no address is given, it asks for one.

## Editing

The runnable `.html` is a self-extracting bundle, so edit the readable source instead:

1. Edit `_template_src.html`.
2. Rebuild: `python3 _rebuild.py` (re-encodes the source and writes both
   `agenticoverlay.html` and `index.html`).
3. Reload in the browser.
