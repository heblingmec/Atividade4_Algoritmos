from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codJuridica, nomeJuridica, endJuridica, telJuridica, cnpj, inscEst, qtdFunc):
        Pessoa.__init__(self, codJuridica, nomeJuridica, endJuridica, telJuridica)
        self._cnpj    = cnpj
        self._inscEst = inscEst
        self.qtdFunc  = qtdFunc

    def imprimeCNPJ(self):
        Pessoa.imprimeNome(self)
        print("CNPJ: ", self._cnpj)
        print("Inscrição Estadual: ", self._inscEst)
        print("Quantidade de Funcionários: ", self.qtdFunc)

    def emitirNotaFiscal(self):
        return None
