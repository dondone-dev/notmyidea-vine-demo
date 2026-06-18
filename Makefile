PELICAN        = pelican
CONFIG         = pelicanconf.py
PUBLISH_CONFIG = publishconf.py
THEME          = themes/notmyidea-vine
SHIKI_CACHE    = .cache/shiki-content

.PHONY: shiki-content dev build clean

shiki-content:
	npm run build:shiki-content

dev: shiki-content
	$(PELICAN) $(SHIKI_CACHE) -s $(CONFIG) -t $(THEME) --autoreload --listen

build: shiki-content
	$(PELICAN) $(SHIKI_CACHE) -s $(PUBLISH_CONFIG)

clean:
	rm -rf output .cache/__pycache__
