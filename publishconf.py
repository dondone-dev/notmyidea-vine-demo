#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Production settings for Cloudflare Pages deployment

from pelicanconf import *

# Replace with your actual CF Pages domain or custom domain
SITEURL = 'https://notmyidea-vine-demo.pages.dev'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'

DELETE_OUTPUT_DIRECTORY = True
