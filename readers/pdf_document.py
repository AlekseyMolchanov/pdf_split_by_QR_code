import os
from PyPDF2 import PdfFileReader, PdfFileWriter

from .interface import DocumentInterface

class PDFDocument(DocumentInterface):
    def __init__(self, source):
        self.source = source
        if not self.source:
            raise ValueError('Source is not set')

        self.__reader = None
        try:
            self.__reader = PdfFileReader(open(self.source, "rb"))
        except Exception as er:
            raise ValueError('Is not PDF [%s]' % self.source)

    def getNumPages(self):
        return self.__reader.getNumPages()

    def getPage(self, page_number):
        return self.__reader.getPage(page_number)

    @property
    def filename(self):
        _, tail = os.path.split(self.source)
        return '.'.join(tail.split('.')[:-1])
