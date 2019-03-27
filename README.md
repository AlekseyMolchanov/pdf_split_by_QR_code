# Dispatch images to folders by the path from QR code
Small tool to split pdf document into pages by QR code or process folder with images

[![CircleCI](https://circleci.com/gh/AlekseyMolchanov/pdf_split_by_QR_code/tree/master.svg?style=svg)](https://circleci.com/gh/AlekseyMolchanov/pdf_split_by_QR_code/tree/master)
[![codecov](https://codecov.io/gh/AlekseyMolchanov/pdf_split_by_QR_code/branch/master/graph/badge.svg)](https://codecov.io/gh/AlekseyMolchanov/pdf_split_by_QR_code)

> all commands available in Makefile

# Usage
Use this script as:

    ./main.py -m <module> <source path>

Example

    ./main.py -m pdf ./samples/pdf/multipage.pdf
    .main.py -m folder ./samples/tiff

# Tests

    pytest -vs

# Docker

build:

    docker build --rm -f "Dockerfile" -t qr_code_split:latest .

run tests:

    docker run -it --rm qr_code_split

run sample:

    > the tool will try find folder inside the container, not in your file system

    ddocker run -it  --rm  -v $$(pwd)/samples/output/pdf:/data --entrypoint "python" qr_code_split main.py -m pdf ./samples/pdf/multipage.pdf

run as script:

    > you must map correct folders and generate right qrcodes

    docker run -it  --rm \
			-v $$(pwd)/Dropbox:/Dropbox \
			-v $$(pwd)/sources:/sources \
			--entrypoint "python" qr_code_split main.py -m pdf ./samples/pdf/multipage.pdf






