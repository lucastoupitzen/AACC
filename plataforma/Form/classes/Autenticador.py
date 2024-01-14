from .utilitarios.Hash import Hash
from .Coordenador import Coordenador
from .Professor import Professor
from .Conector import Conector



class Autenticador():

    def __init__(self):
        pass

    @classmethod
    def hash_senha(cls, senha):
        return senha

    def autenticar(self, id, senha):

        dados = Conector().get_conexao_login(id)

        if dados:
      
            if Hash().conferir_hash(senha, dados.get("senha_hash")):
                print("Logado com sucesso")
                return self.retornar_autenticação(dados.get("usuario"))
            else: 
                print("Senha incorreta!")
                return None
                    
        return None
    

    @classmethod
    def retornar_autenticação(cls, nrousp):

        info = Conector().get_info_user(nrousp)
        print(info)
        if info.get("cargo") == "coordenador":
            coordenador = Coordenador(info.get("nrousp"), info.get("nome"))
            return coordenador
        else:
            professor = Professor(info.get("nrousp"), info.get("nome"))
            return professor
        
    