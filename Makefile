.PHONY: build

build: *.yaml
	@echo "Compiling: $(*.yaml)"

*.yaml: 
	@echo "Compiling: $@"
	@docker run -v "$(shell pwd):/input" resme:latest -i /input/$@ > $(basename $@).tex

clean:
	rm -f *.tex
