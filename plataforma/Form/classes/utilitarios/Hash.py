import bcrypt

class Hash():

    def __init__(self):
        pass

    # métodos para construção e conferência do hashing

    def criar_hash(self, senha):
        
        # Gera um salt aleatório usando o bcrypt
        salt = bcrypt.gensalt()

        # Gera a senha hash usando o bcrypt
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

        # Retorna apenas a senha hash (pode ser armazenada no banco de dados)
        return senha_hash

    def conferir_hash(self, senha, senha_armazenada):

        return bcrypt.checkpw(senha.encode('utf-8'), senha_armazenada.encode('utf-8'))