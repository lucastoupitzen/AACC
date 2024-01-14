import os
import json
from .Conector import Conector

class CRUD_BD():

    def __init__(self) -> None:
        pass

   
    
    def read_AACC_avaliadas(self):
        conexao = Conector.get_conexao_AACC()
        dados_retornados = []
        for dado in conexao:
            if dado["status"] == 2:
                dados_retornados.append(dado)
        return dados_retornados

    def create_delegacao_AACC(self, id_AACC, id_avaliador):
        conexao = Conector.get_conexao_AACC_para_avaliacao()
        novo_dado = {
            "id_aacc": id_AACC,
            "id_avaliador": id_avaliador,
            "data_avaliacao": ""
        }

        conexao.append(novo_dado)

        with open('./mock_BD/AACC_para_avaliacao.json', 'w') as arquivo:
            json.dump(conexao, arquivo, indent=2) 

        # mudar o status da AACC
        self.update_status_AACC(id_AACC, 1)

    def update_status_AACC(self, id_AACC, status):
        conexao = Conector.get_conexao_AACC()
        for dado in conexao:
            if dado.get("id_aacc") == id_AACC:
                dado["status"] = status
                with open('./mock_BD/AACC_para_avaliacao.json', 'w') as arquivo:
                    json.dump(conexao, arquivo, indent=2) 
