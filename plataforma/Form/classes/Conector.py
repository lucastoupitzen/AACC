import json
import os
from ...models import *

class Conector():

    def __init__(self) -> None:
        pass


    def get_info_user(self, nrousp):
        try:
            conexao = User.objects.filter(username=nrousp)
            dados = {
                "username": conexao[0].nrousp,
                "email": conexao[0].email,
                "first_name": conexao[0].nome,
                "last_name": conexao[0].cargo
            }
            return dados
        except: 
            return None
    
    def get_conexao_AACC_nao_encaminhadas(self):
         
        try:
            conexao = AACC.objects.filter(status=0)
            dados = {}
            for dado in conexao:
                dados[dado.id_aacc] = {
                    "aluno": dado.aluno,
                    "status": dado.status,
                    "data_envio": dado.data_envio,
                    "doc": dado.doc
                }
            return dados
        except: 
            return None
        
    def get_conexao_AACC_para_avaliacao():
        #retorna o arquivo json mockado
        caminho_arquivo_json = './mock_BD/AACC_para_avaliacao.json'

        # Verifica se o arquivo existe
        if os.path.exists(caminho_arquivo_json):
            # Abre o arquivo JSON e carrega os dados
            with open(caminho_arquivo_json, 'r') as arquivo:
                dados_json = json.load(arquivo)
                
            return dados_json
        else:
            print(f'O arquivo {caminho_arquivo_json} não foi encontrado.')
            return None
        
    def set_AACC_encaminhada(self, id_aacc, id_avaliador):
        try:
            novo_registro = AACC_para_avaliacao.objects.create(
                id_avaliador=User.objects.get(username=id_avaliador),
                id_aacc=AACC.objects.get(id_aacc= id_aacc)
            )
            novo_registro.save()
            return novo_registro
        except:
            return None
        
    def set_AACC_status(self, id_aacc, status):
        try: 
            aacc = AACC.objects.get(id_aacc=id_aacc)
            aacc.status = status
            aacc.save()
        except:
            return None
