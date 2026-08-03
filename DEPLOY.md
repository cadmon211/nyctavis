# Deploy & setup guide

This repo is both the **GitHub showcase** and the **website** (`index.html`).

## 0. Before you publish — 3 quick edits

1. **Replace the GitHub links.** In `index.html` and `README.md`, change every
   `cadmon211/nyctavis` to your real GitHub path (e.g. `sebastian/nyctavis`).
2. **Add real screenshots.** Drop three PNGs into `assets/`:
   - `screenshot-dashboard.png`
   - `screenshot-recommendations.png`
   - `screenshot-quarantine.png`
   (Take them from the running app — the README and site already point to these names.)
3. **Set your contact email** if it isn't `hello@nyctavis.com` (search & replace).

## 1. Create the GitHub repo

```bash
cd nyctavis-showcase
git init
git add -A
git commit -m "NYCTAVIS showcase site + README"
git branch -M main
git remote add origin https://github.com/cadmon211/nyctavis.git
git push -u origin main
```

## 2. Publish the website on Cloudflare Pages (recommended — your domains are there)

1. In the Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git**.
2. Pick the `nyctavis` repo. Framework preset: **None**. Build command: *(empty)*.
   Build output directory: **`/`** (the root, since `index.html` is at the root).
3. Deploy. You'll get a `*.pages.dev` URL.
4. **Custom domains** → add **`nyctavis.com`** (and `www` if you want) and
   **`nyctavis.app`**. Cloudflare wires DNS automatically since the domains
   live in your account. `.app` is HTTPS-only (HSTS) — Cloudflare's free SSL
   covers it.

### Alternative: GitHub Pages
Settings → Pages → deploy from `main` / root. Then add a `CNAME` file containing
`nyctavis.com` and point the domain's DNS to GitHub. (Cloudflare Pages is simpler here.)

## 3. Optional: redirect `.app` → `.com` (or serve both)
You can either serve the same site on both domains (done automatically if you add
both as custom domains) or, in Cloudflare → the `.app` zone → **Redirect Rules**,
send `nyctavis.app/*` to `https://nyctavis.com/$1` (301).

## 4. Store link

The public Microsoft Store listing is live at:

`https://apps.microsoft.com/detail/9NCP8J7FT020`

Keep this canonical product link in the website and README when updating launch copy.
