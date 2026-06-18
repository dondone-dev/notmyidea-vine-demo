Title: Theme Features Showcase
Date: 2024-01-15
Category: Technology
Tags: theme, pelican, markdown, demo
Summary: A showcase of notmyidea-vine theme features including code blocks, lists, and typography.

This post demonstrates the visual features of the notmyidea-vine theme.

## Typography

Regular paragraph text looks clean and readable. You can use **bold**, *italic*, and `inline code`.

> Blockquotes are styled distinctly to draw attention to important quotes or callouts.

## Code Blocks

Python example:

```python
import pelican

def build_site(settings_file="pelicanconf.py"):
    """Build a Pelican site from the given settings."""
    pelican.main(argv=["-s", settings_file])

if __name__ == "__main__":
    build_site()
```

Shell commands:

```bash
# Install dependencies
pip install -r requirements.txt

# Build the site locally
pelican content

# Serve locally for development
pelican --listen
```

## Lists

Unordered list:

- Item one
- Item two
- Item three with a longer description to show text wrapping behavior

Ordered list:

1. First step: clone the repo
2. Second step: install dependencies
3. Third step: configure `pelicanconf.py`
4. Fourth step: deploy to Cloudflare Pages

## Links and Images

Visit the [Pelican documentation](https://docs.getpelican.com/) for full configuration reference.

## Tables

| Setting | Default | Description |
|---------|---------|-------------|
| `THEME` | — | Path to the theme directory |
| `DEFAULT_LANG` | `en` | Default language |
| `DEFAULT_PAGINATION` | `10` | Articles per page |
| `TIMEZONE` | `UTC` | Site timezone |
