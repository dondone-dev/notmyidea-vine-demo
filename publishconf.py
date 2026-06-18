#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Production settings for Cloudflare Pages deployment

import os
import sys

# Ensure the project root is importable so `from pelicanconf import *` works
# regardless of how Pelican is invoked (make build / wrangler / CF dashboard).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pelicanconf import *

# Replace with your actual CF Pages domain or custom domain
SITEURL = 'https://notmyidea-vine.dondone.dev'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'

DELETE_OUTPUT_DIRECTORY = True
