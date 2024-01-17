import json
from ..classes.Conector import Conector

class crud_AACC():

    def __init__(self) -> None:
        pass

    def read_AACC_nao_delegadas(self):
        return Conector().get_conexao_AACC_nao_encaminhadas()
    
    def read_AACC_nao_avaliadas(self, id_avaliador):
        return Conector().get_conexao_AACC_nao_avaliadas(id_avaliador)
    
    def update_AACC_status(self, id_aacc, status):
        return Conector().set_AACC_status(id_aacc, status)
    
    def read_AACC_nao_confirmadas(self):
        return Conector().get_conexao_AACC_nao_confirmadas()