import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
    
    def abrir_conta(self, conta):
        self.contas.append(conta)
    
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"

class Conta:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []
    
    def depositar(self, valor):
        self.saldo += valor
        self.registrar_transacao(f"Depósito: +{valor}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.registrar_transacao(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente.")
    
    def registrar_transacao(self, descricao):
        data_hora = datetime.datetime.now()
        self.transacoes.append((data_hora, descricao))
    
    def extrato(self):
        print(f"Extrato da Conta {self.numero_conta}:")
        for data_hora, descricao in self.transacoes:
            print(f"{data_hora}: {descricao}")
        print(f"Saldo atual: {self.saldo}")

class ContaCorrente(Conta):
    def __init__(self, numero_conta, tipo_conta="Corrente", saldo=0):
        super().__init__(numero_conta, saldo)
        self.tipo_conta = tipo_conta

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, taxa_juros, tipo_conta="Poupança", saldo=0):
        super().__init__(numero_conta, saldo)
        self.tipo_conta = tipo_conta
        self.taxa_juros = taxa_juros
    
    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.depositar(juros)
        self.registrar_transacao(f"Juros: +{juros}")


if __name__ == "__main__":
    # Criando clientes
    cliente1 = Cliente("João", "123.456.789-00")
    cliente2 = Cliente("Maria", "987.654.321-00")

    # Abrindo contas para os clientes
    conta1 = ContaCorrente("001", saldo=1000)
    conta2 = ContaPoupanca("002", taxa_juros=0.05, saldo=500)

    cliente1.abrir_conta(conta1)
    cliente2.abrir_conta(conta2)

    # Realizando operações bancárias
    conta1.depositar(500)
    conta1.sacar(200)

    conta2.depositar(1000)
    conta2.calcular_juros()

    # Exibindo extratos das contas
    print(cliente1)
    conta1.extrato()

    print("\n")

    print(cliente2)
    conta2.extrato()