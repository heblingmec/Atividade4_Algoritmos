class Pessoa:

    def __init__(self, codigo, nome, endereco, telefone = None):
        self._codigo    = codigo
        self.nome       = nome
        self.__endereco = endereco
        self._telefone  = telefone

    def imprimeNome(self):
        print("-"*37)
        print("Código:   ", self._codigo)
        print("Nome:     ", self.nome)
        print("Endereço: ", self.__endereco)
        print("Telefone: ", self._telefone)
