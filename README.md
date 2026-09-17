# English Outside the Box — website

Static rebuild of [englishoutsidethebox.com](https://www.englishoutsidethebox.com/) for Jennifer Nascimento. Plain HTML/CSS, no framework, hosted on Vercel.

- `build.py` generates `public/` from the hand-written pages in the script, the legacy WordPress pages in `source/pages/`, the blog posts in `source/posts_*.json`, and the podcast RSS in `source/podcast.rss`.
- `assets/` holds the stylesheet, JS, her photos, the Higgsfield-refreshed logo, and the flat illustrations.
- Rebuild: `pip install -r requirements.txt && python3 build.py`. Commit `public/` — Vercel serves it as-is.

All original URLs are preserved (`/englishsuccesssystem/`, `/2015/06/12/…/`, etc.) so her domain can be pointed here without breaking links.
