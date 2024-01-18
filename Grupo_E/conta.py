
from cliente import Cliente  # Importa a classe Cliente

class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de KZ {valor} realizado. Novo saldo: KZ {self.saldo}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de KZ {valor} realizado. Novo saldo: KZ {self.saldo}')
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo atual: KZ {self.saldo}')

    def transferir(self, outra_conta, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            outra_conta.depositar(valor)
            print(f'Transferência de KZ {valor} realizada para a Conta {outra_conta.numero}.')
        else:
            print('Saldo insuficiente para transferência.')

class ContaSalario(Conta):
    def __init__(self, numero, saldo, cliente, salario):
        super().__init__(numero, saldo, cliente)
        self.salario = salario

class ContaPoupanca(Conta):
    def __init__(self, numero, saldo, cliente, juros):
        super().__init__(numero, saldo, cliente)
        self.juros = juros

    def calcular_juros(self):
        self.saldo += self.saldo * (self.juros / 100)
        print(f'Juros aplicados. Novo saldo: KZ {self.saldo}')