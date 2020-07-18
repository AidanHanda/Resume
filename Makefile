.PHONY: build

build: *.yaml
	@echo "Compiling: $(*.yaml)"

*.yaml: 
	@echo "Compiling: $@"
	@echo "$(shell pwd)"
	@docker run -v "$(shell pwd):/input" resme:latest -i /input/AidanHandaResume.yaml
