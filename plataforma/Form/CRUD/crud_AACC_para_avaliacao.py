from ..classes.Conector import Conector

class crud_AACC_para_avaliacao():

    def __init__(self) -> None:
        pass

    def create_AACC_encaminhada(self, id_aacc, id_avaliador):
        return Conector().set_AACC_encaminhada(id_aacc, id_avaliador)
    
    def read_AACC_encaminhada(self, id_avaliador):
        return Conector().get_AACC_encaminhada(id_avaliador)
    
    def update_AACC_para_avaliacao(self, id_AACC, comentarios, status):
        return Conector().set_AACC_avaliada(id_AACC, comentarios, status)