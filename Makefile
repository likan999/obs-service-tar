prefix = /usr
PYTHON ?= python

servicedir = ${prefix}/lib/obs/service

all:

install:
	install -d $(DESTDIR)$(servicedir)
	install -m 0755 tar_utils $(DESTDIR)$(servicedir)
	install -m 0644 tar_utils.service $(DESTDIR)$(servicedir)

.PHONY: all install
