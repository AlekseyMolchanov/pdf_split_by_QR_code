
from abc import ABCMeta, abstractmethod, abstractproperty

class DocumentInterface( metaclass=ABCMeta ):

    @abstractmethod
    def getNumPages(self):
        raise NotImplementedError('users must define getNumPages to use this base class')

    @abstractmethod
    def getPage(self, page_number):
        raise NotImplementedError('users must define getPage to use this base class')

    @abstractproperty
    def filename(self):
        raise NotImplementedError('users must define property filename to use this base class')
