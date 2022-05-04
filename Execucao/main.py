
from Banco_Autenticacao.autenticar import Autenticar
from Contas.conta_poupanca import ContaPoupanca
from Contas.conta_corrente import ContaCorrente
from Pessoas.cliente import Cliente

valida = Autenticar()

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

#  criando cliente
cliente1 = Cliente(nome='Eduardo', idade=33)
cliente2 = Cliente(nome='Julha', idade=34)
cliente3 = Cliente(nome='Alice', idade=18)

#  criando conta
conta1 = ContaPoupanca(agencia=1111, conta=880, saldo=0)
conta2 = ContaCorrente(agencia=2222, conta=881, saldo=0)
conta3 = ContaPoupanca(agencia=1232, conta=882, saldo=0)

#  associando cliente com a conta
cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

#  inserindo cliente e conta no banco autenticar
valida.inserir_cliente(cliente=cliente1)
valida.inserir_conta(conta=conta1)

valida.inserir_cliente(cliente=cliente2)
valida.inserir_conta(conta=conta2)

valida.inserir_cliente(cliente=cliente3)
valida.inserir_conta(conta=conta3)

#  verificando a autenticação
if valida.autenticacao(cliente1):
    cliente1.conta.depositar(50)
    cliente1.conta.sacar(40)
else:
    print('Cliente nao autenticado')

print('\n############################################\n')

if valida.autenticacao(cliente2):
    cliente2.conta.depositar(50)
    cliente2.conta.sacar(60)
else:
    print('Cliente nao autenticado')

print('\n############################################\n')

if valida.autenticacao(cliente3):
    cliente3.conta.depositar(50)
    cliente3.conta.sacar(40)
else:
    print('Cliente nao autenticado')

print('\n############################################\n')
