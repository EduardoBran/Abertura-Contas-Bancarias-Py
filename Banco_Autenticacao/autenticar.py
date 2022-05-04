class Autenticar:

    def __init__(self):
        self.agencias = [1111, 1112, 1113, 1114, 1115]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticacao(self, cliente):

        if cliente not in self.clientes:  # necessario por causa do valida.inserir_cliente(cliente=cliente1) de main
            print('Cliente não encontrado.')
            return False

        if cliente.conta not in self.contas:  # nao precisa
            print('Conta não encontrado.')
            return False

        if cliente.conta.agencia not in self.agencias:
            print('Agência não encontrada.')
            return False

        return True
