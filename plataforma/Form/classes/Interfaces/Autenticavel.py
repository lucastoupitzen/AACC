import abc

class Autenticavel(abc.ABC):

    @abc.abstractmethod
    def realizar_autenticação(self): pass

