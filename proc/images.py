import os

from .interface import DocumentInterface
from tempfile import NamedTemporaryFile
from wand.image import Image as WAND_Image


class ImageFolder(DocumentInterface):
    def __init__(self, source):
        self.source = source
        self.source_files = {}
        if not self.source:
            raise ValueError('Source is not set')

        if not os.path.isdir(self.source):
            raise ValueError('Is not valid source [%s]' % self.source)

        for _path, _folders, _files in os.walk(self.source):
            for page_number, each in enumerate(sorted(_files)):
                self.source_files[page_number] = os.path.join(_path, each)

    def getNumPages(self):
        return len(self.source_files.keys())

    def getPage(self, page_number):
        return open(self.source_files[page_number], 'rb')

    def getTemporaryPage(self, page_number):
        tmp = self.getPage(page_number)
        with NamedTemporaryFile(delete=False) as out:
            with WAND_Image(filename=tmp.name, resolution=150) as img:
                img.format = 'jpg'
                img.save(file=out)
                out.close()
                return out

    def get_filename(self, uuid):
        return "{}_{}.tif" .format(os.path.basename(self.source), uuid)

    def savePage(self, num, path):
        fh = self.getPage(num)
        try:
            with open(path, 'wb') as output:
                output.write(fh.read())
                return ('ok', self.source, num, path)
        except Exception as ex:
            return (ex, self.source, num, path)
