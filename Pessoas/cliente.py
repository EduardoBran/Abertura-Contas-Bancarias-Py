from Pessoas.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super(Cliente, self).__init__(nome, idade)

    def inserir_conta(self, conta):
        self.conta = conta