#!/usr/bin/env python
# encoding: utf-8

import sys
from tool import Tool
from readers import PDFDocument
USAGE = '''
Use this script as:
    ./main.py <source file path>

    Example:
    ./main.py sample.pdf
'''

def process(source):
    try:
        reader = PDFDocument(source)
        tool = Tool(reader)
        for each in tool.files:
            print(each.save())
    except Exception as e:
        print(e)
        return 2
    return 0

def main(_, source = None, *args):
    if args or not source:
        print (USAGE)
        return 1
    return process(source)

if __name__ == "__main__":
    exit(main(*list(sys.argv or [])))
