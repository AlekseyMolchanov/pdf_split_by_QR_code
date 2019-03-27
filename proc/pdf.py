import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tempfile import NamedTemporaryFile
from wand.image import Image as WAND_Image

from .interface import DocumentInterface


class PDFDocument(DocumentInterface):
    def __init__(self, source):
        self.source = source
        if not self.source:
            raise ValueError('Source is not set')

        self.__reader = None
        try:
            self.__reader = PdfFileReader(open(self.source, "rb"), strict=False)
        except Exception as er:
            raise ValueError('Is not valid source [%s]' % self.source)

    def getNumPages(self):
        return self.__reader.getNumPages()

    def getPage(self, page_number):
        return self.__reader.getPage(page_number)

    def getTemporaryPage(self, num):
        page = self.getPage(num)

        with NamedTemporaryFile(delete=False) as tmp:

            wrt = PdfFileWriter()
            wrt.addPage(page)
            wrt.write(tmp)
            tmp.close()

            with NamedTemporaryFile(delete=False) as out:

                with WAND_Image(filename=tmp.name, resolution=150) as img:
                    img.format = 'jpg'
                    img.save(file=out)

                out.close()

                os.unlink(tmp.name)

                return out

    def get_filename(self, uuid):
        _, tail = os.path.split(self.source)
        _filename = '.'.join(tail.split('.')[:-1])
        return "{}_{}.pdf" .format(_filename, uuid)

    def savePage(self, num, path):
        page = self.getPage(num)
        try:
            with open(path, 'wb') as output:
                wrt = PdfFileWriter()
                wrt.addPage(page)
                wrt.write(output)
                return ('ok', self.source, num, path)
        except Exception as ex:
            return (ex, self.source, num, path)
