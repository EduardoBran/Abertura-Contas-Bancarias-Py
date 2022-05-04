from Banco_Autenticacao.autenticar import Autenticar
from Contas.conta_poupanca import ContaPoupanca
from Contas.conta_corrente import ContaCorrente
from Pessoas.cliente import Cliente
from Contas.conta import Conta
import time
from random import randint

valida = Autenticar()


def cronometro(v):
    if v == 1:
        num_of_secs = 3
        while num_of_secs:
            print('.')
            time.sleep(1)
            num_of_secs -= 1
        input('Digite qualquer tecla para continuar...')
        print('\n' * 30)

    if v == 2:
        num_of_secs = 1
        while num_of_secs:
            print('.\n' * 30)
            time.sleep(1)
            num_of_secs -= 1


def menu_opcoes():
    print('\n\nQual serviço gostaria de realizar?\n')
    print('\t1- Depósito')
    print('\t2- Saque')
    print('\t3- Informações')
    print('\t4- Retornar ao início')
    print('\t5- Encerrar')


def validando(cliente, conta):
    cliente.inserir_conta(conta)
    valida.inserir_cliente(cliente)
    valida.inserir_conta(conta)

    if valida.autenticacao(cliente):

        flag = True

        while flag:
            menu_opcoes()
            op = input('\nOpção escolhida: ')

            if op == '1':
                valor = int(input('\nQual valor vc gostaria de depositar? R$'))
                cliente.conta.depositar(valor)
            elif op == '2':
                valor = int(input('\nQual valor vc gostaria de sacar? R$'))
                cliente.conta.sacar(valor)
            elif op == '3':
                print(f'\n *** Info da conta de {cliente.nome} ***:\n')
                Conta.detalhes(self=conta)
            elif op == '4':
                inicio()
            else:
                print('\n *** Programa Encerrado ***')
                exit()
    else:
        print('Cliente nao autenticado')


def abrir_conta(cliente, tipo):
    flag = True
    while flag:
        agencia = input('\n\nDigite o número da agência escolhida (1111 - 1115): ')
        conta = randint(4001, 4999)
        print('\nGerando o número da sua conta...')
        cronometro(1)

        try:
            agencia = int(agencia)

            if tipo == 1:
                conta = ContaPoupanca(agencia=agencia, conta=conta, saldo=0)
                validando(cliente, conta)

            if tipo == 2:
                conta = ContaCorrente(agencia=agencia, conta=conta, saldo=0)
                validando(cliente, conta)

        except ValueError as e:
            s = input(
                "\nFormato de agência inválido. Digite qualquer tecla para voltar ou aperte 's' para sair: ").lower()
            if s == 's':
                print('\n *** Programa Encerrado ***')
                exit()
            cronometro(2)


def inicio():
    flag = True
    while flag:
        print('\n*** Sistema Bancário para Abertura de Contas ***')
        nome = input('\nPor favor informe seu nome: ')

        if any(chr.isdigit() for chr in nome):
            print('\nNome inválido.')
            cronometro(1)
            inicio()
        else:
            idade = input('Diga sua idade: ')
            try:
                idade = int(idade)

                if idade < 18:
                    print('De menor. Nao pode')
                    cronometro(1)
                    inicio()
                else:
                    cronometro(2)
                    print(f'\tSeja Bem Vindo {nome}')
                    cliente = Cliente(nome=nome, idade=idade)
                    print('\nDigite o tipo de conta que gostaria de abrir:\n')
                    print('\t1 - Conta Poupança')
                    print('\t2 - Conta Corrente')
                    op = input('\nOpção: ')

                    if op == '1':
                        abrir_conta(cliente, 1)
                    elif op == '2':
                        abrir_conta(cliente, 2)
                    else:
                        print('Opção Inválida')
                        cronometro(1)
                        inicio()

            except ValueError as e:
                print('Idade inválida.')
                cronometro(1)


inicio()
