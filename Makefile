sample:
	python main.py ./sample.pdf

test:
	pytest -vs

build:
	docker build --rm -f "Dockerfile" -t qr_code_split:latest .

clear_build:
	docker build --no-cache --rm -f "Dockerfile" -t qr_code_split:latest .

docker_test:
	docker run -it --rm qr_code_split

docker_sample:
	docker run -it  --rm  -v $$(pwd)/samples/output/pdf:/data --entrypoint "python" qr_code_split main.py -m pdf ./samples/pdf/multipage.pdf
	docker run -it  --rm  -v $$(pwd)/samples/output/tiff:/data --entrypoint "python" qr_code_split main.py -m folder ./samples/tiff