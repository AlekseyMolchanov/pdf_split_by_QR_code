
from abc import ABCMeta, abstractmethod, abstractproperty

class DocumentInterface( metaclass=ABCMeta ):

    @abstractmethod
    def getNumPages(self):
        raise NotImplementedError('users must define getNumPages to use this base class')

    @abstractmethod
    def getPage(self, page_number):
        raise NotImplementedError('users must define getPage to use this base class')

    @abstractmethod
    def getTemporaryPage(self, page_number):
        raise NotImplementedError('users must define getTemporaryPage to use this base class')

    @abstractmethod
    def get_filename(self, page_number):
        raise NotImplementedError('users must define get_filename to use this base class')

    @abstractmethod
    def savePage(self, page_number):
        raise NotImplementedError('users must define savePage to use this base class')



