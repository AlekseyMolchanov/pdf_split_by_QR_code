# encoding: utf-8

import sys, os
import argparse
from tool import Tool
from proc import PDFDocument, ImageFolder

import logging
logging.basicConfig()
logger = logging.getLogger('qrcode_tool')
logger.setLevel(logging.DEBUG)

Modes = dict(
    pdf=PDFDocument,
    folder=ImageFolder
)

def process(cls, source):
    try:
        reader = cls(source)
        tool = Tool(reader, logger=logger)
        for each in tool.files:
            print(each.save())
    except Exception as e:
        print(e)
        return 2
    return 0

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-m', help='mode', default='pdf')
    parser.add_argument('source', help='source path')
    args = parser.parse_args()
    return process(Modes.get(args.m), os.path.abspath(args.source))

if __name__ == "__main__":
    exit(main())
