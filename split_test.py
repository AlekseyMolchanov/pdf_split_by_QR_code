#!/usr/bin/env python
# encoding: utf-8

import os
import pytest

from tool import Tool
from readers import PDFDocument

INPUT_FILE_NULL = None
INPUT_FILE_INVALID = 'invalid.pdf'
INPUT_FILE_VALID = 'sample.pdf'
FILE_IMAGE_PNG = 'sample.png'
FOLDERS = [
    'C:/dms/reports/',
    'C:/dms/notes/',
]
DIRECTORIES_COUNT = len(FOLDERS)
PAGES_COUNT = 6
FILES_COUNT = 4


def test_wand_pdf_to_png():

    from wand.image import Image

    with open(FILE_IMAGE_PNG, 'wb') as out:
        with Image(filename=INPUT_FILE_VALID, resolution=300) as img:
            img.compression_quality = 100
            img.format = 'png'
            img.save(file=out)

    with open(FILE_IMAGE_PNG, 'rb') as test:
        assert test.read()


# 1. Input

def test_empty_input_file():
    #
    # 1. Assert exception if input.file == null or empty
    #
    with pytest.raises(ValueError, match=r'Source is not set'):
        tool = Tool()

def test_null_input_file():
    #
    # 1. Assert exception if input.file == null or empty
    #
    with pytest.raises(ValueError, match=r'Source is not set'):
        reader = PDFDocument(INPUT_FILE_NULL)
        tool = Tool(reader)

def test_not_PDF_input_file():
    #
    # 2. Assert exception if input.file != filetype pdf
    #
    with pytest.raises(ValueError, match=r'Is not PDF .*'):
        reader = PDFDocument(INPUT_FILE_INVALID)
        tool = Tool(reader)

def test_PDF_input_file():
    #
    # 2. Assert exception if input.file == filetype pdf
    #
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    assert tool

def test_input_file_page_count():
    #
    # 3. Assert exception if input.pdf.page.size != 6
    #
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    assert tool.pages_count == PAGES_COUNT
    assert len(tool.pages) == PAGES_COUNT

def test_input_file_qrcodes_count():
    #
    # 4. Assert exception if input.file.qrcode.count < 1
    #
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    assert len(tool.qrcodes)

def test_input_file_each_qrcode_is_valid_path():
    #
    # 5. Assert exception for each if input.file.qrcode != file path format
    #
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    for qrcode in tool.qrcodes:
        assert qrcode in FOLDERS


# # 2. Output

def test_each_output_directories_fullpath_is_one_of_input_qrcode_value():
    #
    # 1. Assert for each output.directories.fullpath is one of input.qrcode.value[]
    #
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    for each in tool.files:
        assert each.folder in FOLDERS

def test_output_directories_count():
    #
    # 2. Assert output.directories.count == 3
    #
    directories = []
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    for each in tool.files:
        if each.folder not in directories:
            directories.append(each.folder)
    assert len(directories) == DIRECTORIES_COUNT

def test_output_files_count():
    #
    # 3. Assert output.files.count == 4
    #
    directories = []
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    assert len(tool.files) == FILES_COUNT

def test_output_files_name():
    #
    # 4. Assert each output.file.name == input.file.name+_+uuid
    #
    input_file_name = INPUT_FILE_VALID.split('.').pop(0)
    reader = PDFDocument(INPUT_FILE_VALID)
    tool = Tool(reader)
    for each in tool.files:
        assert (each.file_name == '{}_{}.pdf'.format(input_file_name, each.uuid))
