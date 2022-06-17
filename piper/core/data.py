from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty


class Data(ABC):
    @abstractmethod
    def data(self):
        pass

    @abstractmethod
    def save(self):
        pass


class BaseData(Data):
    
    _LOADERS = [
        CsvLoader
    ]


    def __init__(self, )