# notmyidea-vine Demo

Demo site for the [notmyidea-vine](https://github.com/dondone-dev/notmyidea-vine) Pelican theme, deployed on Cloudflare Pages.

## Repository Structure

```
notmyidea-vine-demo/
├── themes/notmyidea-vine/   # Theme (git submodule)
├── plugins/                 # Pelican plugins (i18n_subsites, sitemap)
├── scripts/
│   └── build_shiki_content.mjs  # Shiki code-highlighting preprocessor
├── content/
│   ├── markdown/            # Articles (.md)
│   ├── pages/               # Static pages (.md)
│   ├── images/              # Images
│   └── extra/               # robots.txt, favicon.ico
├── .cache/shiki-content/    # Pre-processed content (git-ignored)
├── Makefile                 # Build targets: dev, build, shiki-content
├── package.json             # Node.js deps (shiki)
├── pelicanconf.py           # Base config (local dev)
├── publishconf.py           # Production config (CF Pages)
├── requirements.txt
└── wrangler.toml            # Cloudflare Pages config
```

## Local Development

The build pipeline runs in two steps: Shiki pre-processes code blocks for syntax highlighting, then Pelican generates the site from the cached output.

```bash
# Clone with submodules
git clone --recurse-submodules https://github.com/dondone-dev/notmyidea-vine-demo.git
cd notmyidea-vine-demo

# Install Node.js dependencies (for Shiki code highlighting)
npm install

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Build and serve with code highlighting (uses local theme)
make dev
# Open http://localhost:8000
```

`make dev` runs `npm run build:shiki-content` (processes `content/` → `.cache/shiki-content/`) then starts Pelican with `--autoreload --listen`.

> **Tip:** Run `make shiki-content` again whenever you add or modify articles, then Pelican's autoreload will pick up the updated cache.

## Cloudflare Pages Deployment

### Via Dashboard

1. Connect this repo in the CF Pages dashboard
2. Set the following build settings:

| Setting | Value |
|---------|-------|
| Build command | `npm install && pip install -r requirements.txt && make build` |
| Build output directory | `output` |

3. After the first deploy, update `SITEURL` in `publishconf.py` to your CF Pages domain

### Via Wrangler CLI

```bash
# Build
make build

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
