# Demo video — honest pattern (no fake media bundled)

GitHub READMEs cannot reliably autoplay video inline. The verified 2026 pattern used here:

1. **Screenshot first** (`docs/images/preview-hero.png`, `preview-market.png`) — real captures from `preview.html` in this repo, taken with a real browser.
2. **Thumbnail that links out** — README wraps the hero image in a link to `preview.html` (or your Pages URL / release video). Click = play/learn.
3. **Add a real recording later** without rewriting anything:
   - Record ≤60s: open `preview.html`, scroll story → markets → quiz, answer 2 questions.
   - Tools that work well: screen recorder → MP4/GIF, `asciinema` or `vhs` for terminal (`bash scripts/run_all.sh`).
   - Keep GIFs small (5–15s, core workflow first); host MP4s in a GitHub Release and link the thumbnail to it.
   - Replace the link target in README + `preview.html` hero; keep the screenshots as fallback.

Do not commit a placeholder video. A linked interactive page beats a fake clip.
