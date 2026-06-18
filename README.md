# notmyidea-vine Demo

*English | [中文](README.zh.md)*

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

### Via Dashboard (recommended)

1. In the Cloudflare dashboard, go to **Workers & Pages → Create → Pages → Connect to Git** and select this repository.
2. On the **Set up builds and deployments** screen, fill in:

   | Setting | Value |
   |---------|-------|
   | **Framework preset** | `None` |
   | **Build command** | `npm install && pip install -r requirements.txt && make build` |
   | **Build output directory** | `output` |
   | **Root directory** | *(leave empty)* |

3. (Recommended) Under **Environment variables**, pin the toolchain versions to avoid build-image defaults that may be too old:

   | Variable | Value |
   |----------|-------|
   | `PYTHON_VERSION` | `3.12` |
   | `NODE_VERSION` | `20` |

4. Click **Save and Deploy**. Git submodules (the theme) are checked out automatically.
5. After the first deploy, set `SITEURL` in `publishconf.py` to your real CF Pages domain (or custom domain) and push again — feeds, sitemap, and absolute image URLs all derive from it.

> **Why the build command lives in the dashboard, not `wrangler.toml`:** Cloudflare Pages does **not** support a `[build]` section in `wrangler.toml` (that is Workers-only syntax) — adding one fails config validation. `wrangler.toml` only carries the project `name` and `pages_build_output_dir`; the build command must be set in the dashboard.

### Via Wrangler CLI

```bash
# Build locally
make build

# Deploy the output/ directory
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
