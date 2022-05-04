from Contas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super(ContaCorrente, self).__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('saldo insuficiente')
            return

        self.saldo -= valor
        print('\n')
        self.detalhes()
