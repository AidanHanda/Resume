.PHONY: build

TEMPDIR = $(basename $@).temp
RESUMES := $(patsubst %.yaml, %.pdf, $(wildcard *.yaml))
TEXBUILDCMD = docker run -v "$(shell pwd):/input" aidanhanda/resme:latest -i /input/$<
XELATEX = $(shell which xelatex)

build: $(RESUMES)

%.pdf: %.yaml 
	@echo "Compiling: $@"
ifeq ($(XELATEX),)
	@echo "XeLaTeX not detected!"
	@echo "Outputting TEX file!"
	@$(TEXBUILDCMD) > $(basename $@).tex
else
	@echo "Creating TEMPDIR: $(TEMPDIR)"
	@mkdir "$(TEMPDIR)"
	@$(TEXBUILDCMD) > $(TEMPDIR)/$(basename $@).tex
	-@cd $(TEMPDIR); xelatex -interaction=batchmode $(basename $@).tex > $(basename $a).xelatex.log
	@mv $(TEMPDIR)/$(basename $@).pdf $(basename $@).pdf
	@echo "Removing temp directory: $(TEMPDIR)"
	@rm -rf $(basename $@).temp
endif



clean:
	rm -f *.tex
	rm -rf *.temp
	rm -f *.pdf
