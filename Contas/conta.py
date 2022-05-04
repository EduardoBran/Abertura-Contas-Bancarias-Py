from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print('\n')
        self.detalhes()

    @abstractmethod
    def sacar(self, valor): ...

    def detalhes(self):
        print(f'Agencia: 0000{self.agencia} '
              f'Conta: 0000{self.conta} '
              f'Saldo: {self.saldo}')
