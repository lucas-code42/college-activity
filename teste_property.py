class Teste:
    def __init__(self):
        self.__nome = 0

    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        return




t1 = Teste()
print(t1.nome)
t1.nome = 'lucas'
print(t1.nome)