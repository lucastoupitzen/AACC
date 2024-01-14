from .Usuario import Usuario
from .Conector import Conector
from .CRUD_BD import CRUD_BD

class Coordenador(Usuario):

    def __init__(self, id, nome):
        super().__init__(id, nome)

    def set_data_inicio(self, data):
        self.data_inicio = data

    def get_data_inicio(self):
        return self.data_inicio
    
    def set_senha_jupiter(self, senha):
        self.senha_jupiter = senha

    # esses três métodos seram implementados em classes separadas,
    # aqui são apenas instanciados os comportamentos do coordenador
    def acessar_AACC_nao_delegadas(self):
        return CRUD_BD().read_AACC_nao_delegadas()


    def delegar_AACC(self, id_prof, id_AACC):
        return CRUD_BD().create_delegacao_AACC(id_AACC, id_prof)
        

    def receber_avaliações(self):
        return CRUD_BD().read_AACC_avaliadas()

    def confirmar_avaliação(self, id_AACC):
        pass