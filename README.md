# notmyidea-vine Demo

Demo site for the [notmyidea-vine](https://github.com/dondone-dev/notmyidea-vine) Pelican theme, deployed on Cloudflare Pages.

## Repository Structure

```
notmyidea-vine-demo/
├── themes/notmyidea-vine/   # Theme (git submodule)
├── plugins/                 # Pelican plugins (i18n_subsites, sitemap)
├── content/
│   ├── markdown/            # Articles (.md)
│   ├── pages/               # Static pages (.md)
│   ├── images/              # Images
│   └── extra/               # robots.txt, favicon.ico
├── pelicanconf.py           # Base config (local dev)
├── publishconf.py           # Production config (CF Pages)
├── requirements.txt
└── wrangler.toml            # Cloudflare Pages config
```

## Local Development

```bash
# Clone with submodules
git clone --recurse-submodules https://github.com/dondone-dev/notmyidea-vine-demo.git
cd notmyidea-vine-demo

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Build and serve (uses the local theme directly)
pelican content -s pelicanconf.py -t ../notmyidea-vine --autoreload --listen
# Open http://localhost:8000
```

> **Tip:** The `-t ../notmyidea-vine` flag points directly to a local clone of the theme repo, so any changes you make to the theme are reflected immediately on refresh without going through the submodule.

## Cloudflare Pages Deployment

### Via Dashboard

1. Connect this repo in the CF Pages dashboard
2. Set the following build settings:

| Setting | Value |
|---------|-------|
| Build command | `pip install -r requirements.txt && pelican content -s publishconf.py` |
| Build output directory | `output` |

3. After the first deploy, update `SITEURL` in `publishconf.py` to your CF Pages domain

### Via Wrangler CLI

```bash
# Build
pelican content -s publishconf.py

# Deploy
wrangler pages deploy output --project-name=notmyidea-vine-demo
```

## Customization

Edit `pelicanconf.py` to configure:
- `SITENAME`, `AUTHOR`, `SITESUBTITLE`
- `MENUITEMS` for navigation
- `INDEX_TITLE`, `INDEX_MESSAGE` for the homepage
- `GISCUS_*` for comments (uncomment the relevant lines)
- Analytics settings

## License

MIT
