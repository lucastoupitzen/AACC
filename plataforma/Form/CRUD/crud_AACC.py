import json
from ..classes.Conector import Conector

class crud_AACC():

    def __init__(self) -> None:
        pass

    def read_AACC_nao_delegadas(self):
        return Conector().get_conexao_AACC_nao_encaminhadas()
    
    def update_AACC_status(self, id_aacc, status):
        return Conector().set_AACC_status(id_aacc, status)