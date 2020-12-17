.PHONY: build-image run rm

build-image:
	docker build -t golang -f Dockerfile .
run: rm
	docker run --name go -itd -v $(PWD):/app golang bash
rm:
	docker rm -f go
