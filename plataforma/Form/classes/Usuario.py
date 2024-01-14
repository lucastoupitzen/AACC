
class Usuario():

    def __init__(self, id, nome):
        super().__init__()
        self.id = id
        self.nome = nome
        

    def get_nome(self):
        return self.nome
    