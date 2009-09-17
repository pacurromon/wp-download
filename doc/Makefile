# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) rst

.PHONY: help all clean html text

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  all	   to make html and text"
	@echo "  html      to make standalone HTML files"
	@echo "  text      to make txt files"
	@echo "  clean     to clean all generated files"

all: html text

clean:
	-rm -rf txt/*
	-rm -rf html/*
	-rm -rf doctrees/

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) html
	@echo
	@echo "Build finished. The HTML pages are in ./html"

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) txt
	@echo
	@echo "Build finished. The txt files are in ./txt"
