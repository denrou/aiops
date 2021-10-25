IMAGE="aiops"

stop:
	docker stop ${IMAGE} || true

build:
	docker build -t ${IMAGE} application/

clean:
	rm -rf data/

run: stop clean build
	docker run --rm --name ${IMAGE} -v /Users/denis/Projects/aiops/data:/app/monitoring -d ${IMAGE}