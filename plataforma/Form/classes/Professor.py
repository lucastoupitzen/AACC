from .Usuario import Usuario

class Professor(Usuario):

    def __init__(self, id, nome):
        super().__init__(id, nome)

    # esses três métodos seram implementados em classes separadas,
    # aqui são apenas instanciados os comportamentos do professor

    def recebe_AACC(self):
        pass

    def avalia(self, id_AACC):
        pass

    def retorna_avaliacao(self, id_AACC):
        pass