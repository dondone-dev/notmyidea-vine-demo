Title: Deploy to Cloudflare Pages
Date: 2024-02-01
Category: Technology
Tags: cloudflare, deployment, pelican, tutorial
Summary: Step-by-step guide to deploying this Pelican site to Cloudflare Pages using the notmyidea-vine theme.

Cloudflare Pages provides free hosting with global CDN, automatic SSL, and Git-based deployments. Here's how to deploy this demo site.

## Prerequisites

- A Cloudflare account (free tier is sufficient)
- This repository forked or cloned to your GitHub/GitLab account

## Method 1: Cloudflare Pages Dashboard (Recommended)

### 1. Connect your repository

1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/)
2. Navigate to **Workers & Pages** → **Create application** → **Pages**
3. Connect your GitHub or GitLab account
4. Select the `notmyidea-vine-demo` repository

### 2. Configure build settings

| Setting | Value |
|---------|-------|
| **Framework preset** | None |
| **Build command** | `pip install -r requirements.txt && pelican content -s publishconf.py` |
| **Build output directory** | `output` |

### 3. Set environment variables (optional)

If you need to override the site URL or other settings, add them as environment variables.

### 4. Deploy

Click **Save and Deploy**. Cloudflare Pages will clone the repo (including the `themes/notmyidea-vine` submodule), install dependencies, build the site, and publish it.

## Method 2: Wrangler CLI

Install [Wrangler](https://developers.cloudflare.com/workers/wrangler/):

```bash
npm install -g wrangler
wrangler login
```

Build the site locally:

```bash
pip install -r requirements.txt
pelican content -s publishconf.py
```

Deploy:

```bash
wrangler pages deploy output --project-name=notmyidea-vine-demo
```

## Updating `publishconf.py`

After your first deployment, update the `SITEURL` in `publishconf.py` to match your actual CF Pages domain:

```python
SITEURL = 'https://your-project.pages.dev'
# or your custom domain:
# SITEURL = 'https://blog.example.com'
```

Commit and push — Cloudflare Pages will redeploy automatically.
