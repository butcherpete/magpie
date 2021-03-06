# Minimal makefile for Sphinx documentation
#

#  cp -r $(SOURCEDIR)/_static/css $(BUILDDIR)/_static/
# Put it first so that "make" without argument is like "make help".

GH_PAGES_SOURCES = source Makefile

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Magpie
SOURCEDIR     = source
BUILDDIR      = build

ALLSPHINXOPTS = source

.PHONY: help Makefile

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: gh-pages
.ONESHELL:
gh-pages:
	rm -rf /tmp/gh-pages
	cp -r $(SOURCEDIR)/_static/css $(BUILDDIR)/html/_static
	cp -r $(BUILDDIR)/html /tmp/gh-pages 
	git checkout gh-pages 
	rm -rf *
	cp -r /tmp/gh-pages/* .
	touch .nojekyll 
	git add .
	git commit -m "Update to gh-pages" 
	git push origin gh-pages 
	git checkout master  


.PHONY: checklinks 
checklinks:
	$(SPHINXBUILD) -b linecheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck  
	@echo
	@echo "Check finished. Look for errors in output " \ 
	@ Report is in $(BUILDDIR)/linecheck/output.txt."
  
  
#	cd .. && rm -rf * && cp -r /tmp/gh-pages/* . & git add . && git commit -m "Updated gh-pages" && git push && git checkout master  


# gh-pages:
# 	git checkout gh-pages
# 	rm -rf build _sources _static 
# 	touch .nojekyll 
# 	git checkout master $(GH_PAGES_SOURCES)
# 	git reset HEAD
# 	make html
# 	mv ./build/html/* ./
# 	rm -rf $(GH_PAGES_SOURCES) build
# 	git add -A
# 	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master
# 	git push origin gh-pages 

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)



