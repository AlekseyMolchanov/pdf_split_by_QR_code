#!/usr/bin/env python
# encoding: utf-8

import io, os, uuid
import zbar
import zbar.misc
from PIL import Image
import numpy


class File(object):
    def __init__(self, tool, num, folder):
        self.tool = tool
        self.num = num
        self.folder = folder
        self.uuid = str(uuid.uuid4())

    @property
    def filename(self):
        return self.tool.io.get_filename(self.uuid)

    def save(self, folder=None):
        path = os.path.join(folder or self.folder, self.filename)
        result = self.tool.io.savePage(self.num, path)
        tmpl = "[%s] from file '%s' copy page (%s) to %s"
        return tmpl % result


class Tool:
    def __init__(self, io=None, logger=None):

        self.io = io
        self.__logger = logger

        self.__pages = {}
        self.__qrcodes = {}

        if not self.io:
            raise ValueError('Source is not set')
        else:
            self.__split_pages()

    @property
    def pages_count(self):
        return self.io.getNumPages()

    @property
    def pages(self):
        return self.__pages.values()

    @property
    def qrcodes(self):
        return sum(self.__qrcodes.values(), [])

    @property
    def files(self):
        __files = []

        folder = None

        for num in self.__pages.keys():
            barcodes = self.__qrcodes.get(num)
            if barcodes and any(barcodes):
                folder = barcodes[0]
            else:
                if not folder:
                    raise ValueError('First page is not QRcode')

                __files.append(File(
                    self,
                    num,
                    folder
                ))
        return __files

    @staticmethod
    def code(file_path, barcode_type='QRCODE'):

        pil = Image.open(file_path).convert('L')
        np_im = numpy.array(pil)

        if len(np_im.shape) == 3:
            np_im = zbar.misc.rgb2gray(np_im)

        barcodes = []
        scanner = zbar.Scanner()

        results = scanner.scan(np_im)
        for barcode in results:
            barcodes.append(barcode.data.decode('utf-8'))
        return barcodes

    def __split_pages(self):
        for num in range(self.pages_count):
            self.__pages[num] = True

            tmp = self.io.getTemporaryPage(num)
            code = Tool.code(tmp.name)
            self.__qrcodes[num] = code

            if os.path.isfile(tmp.name):
                os.unlink(tmp.name)
