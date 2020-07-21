.PHONY: build

TEMPDIR = $(basename $@).temp
RESUMES := $(patsubst %.yaml, %.pdf, $(wildcard *.yaml))

build: $(RESUMES)
	@echo "Compiling: $(*.yaml)"

%.pdf: %.yaml 
	@echo "Compiling: $@"
	@echo "Creating TEMPDIR: $(TEMPDIR)"
	@mkdir "$(TEMPDIR)"
	@docker run -v "$(shell pwd):/input" aidanhanda/resme:latest -i /input/$< > $(TEMPDIR)/$(basename $@).tex
	-@cd $(TEMPDIR); xelatex -interaction=batchmode $(basename $@).tex
	@mv $(TEMPDIR)/$(basename $@).pdf $(basename $@).pdf
	@rm -rf $(basename $@).temp



clean:
	rm -f *.tex
	rm -rf *.temp
	rm -f *.pdf
