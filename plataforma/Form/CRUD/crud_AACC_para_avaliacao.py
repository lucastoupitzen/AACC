from ..classes.Conector import Conector

class crud_AACC_para_avaliacao():

    def __init__(self) -> None:
        pass

    def create_AACC_encaminhada(self, id_aacc, id_avaliador):
        return Conector().set_AACC_encaminhada(id_aacc, id_avaliador)