
from cliente import Cliente  # Importa a classe Cliente
from conta import Conta, ContaSalario, ContaPoupanca  # Importa as classes de Conta

            
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome, sexo, data_nascimento):
        cliente = Cliente(nome, sexo, data_nascimento)
        self.clientes.append(cliente)
        import os
        os.system("clear")
        print(f'Cliente {nome} cadastrado.')

    def consultar_cliente(self, nome_cliente):
        for cliente in self.clientes:
            if cliente.nome == nome_cliente:
                print(f'Informações do Cliente {nome_cliente}:')
                print(f'Nome: {cliente.nome}')
                print(f'Sexo: {cliente.sexo}')
                print(f'Data de Nascimento: {cliente.data_nascimento}')
                import os
                os.system("clear")
                return
        print(f'Cliente {nome_cliente} não encontrado.')

    def extrato_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta:
                print(f'Extrato da Conta {numero_conta}:')
                print(f'Cliente: {conta.cliente.nome}')
                print(f'Saldo Atual: KZ {conta.saldo}')
                import os
                os.system("clear")
                return
        print(f'Conta {numero_conta} não encontrada.')

    def abrir_conta(self, cliente, tipo_conta):
        numero_conta = len(self.contas) + 1

        if tipo_conta == 'Salario':
            conta = ContaSalario(numero_conta, 0, cliente, 0)
        elif tipo_conta == 'Poupanca':
            conta = ContaPoupanca(numero_conta, 0, cliente, 2)  
        else:
            print('Tipo de conta não reconhecido.')
            return
            
        self.contas.append(conta)
        import os
        os.system("clear")
        print(f'Conta {numero_conta} aberta para o cliente {cliente.nome}.')
        

    def fechar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta:
                self.contas.remove(conta)
                print(f'Conta {numero_conta} fechada.')
                return
            import os
            os.system("clear")
        print(f'Conta {numero_conta} não encontrada.')
            

banco = Banco()

while True:
    print("\n1 - Cadastrar Cliente")
    print("2 - Abrir Conta")
    print("3 - Fechar Conta")
    print("4 - Realizar Operações Bancárias")
    print("5 - Consultar Cliente")
    print("6 - Extrato da Conta")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")
    import os
    os.system("clear")
    if escolha == "1":
        nome = input("Digite o nome do cliente: ")
        sexo = input("Digite o sexo do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente (formato YYYY-MM-DD): ")
        banco.cadastrar_cliente(nome, sexo, data_nascimento)

    elif escolha == "2":
        nome_cliente = input("Digite o nome do cliente: ")
        tipo_conta = input("Digite o tipo de conta (Salario/Poupanca): ")
        cliente = None
        for c in banco.clientes:
            if c.nome == nome_cliente:
                cliente = c
                break
        if cliente:
            banco.abrir_conta(cliente, tipo_conta)
        else:
            print(f'Cliente {nome_cliente} não encontrado.')

    elif escolha == "3":
        numero_conta = int(input("Digite o número da conta a ser fechada: "))
        banco.fechar_conta(numero_conta)

    elif escolha == "4":
        numero_conta = int(input("Digite o número da conta para operações: "))
        for conta in banco.contas:
            if conta.numero == numero_conta:
                while True:
                    print("\n1 - Depositar")
                    print("2 - Sacar")
                    print("3 - Consultar Saldo")
                    print("4 - Transferir")
                    print("0 - Voltar")

                    opcao = input("Escolha uma opção: ")
                    import os
                    os.system("clear")
                    if opcao == "1":
                        valor = float(input("Digite o valor a ser depositado: "))
                        conta.depositar(valor)

                    elif opcao == "2":
                        valor = float(input("Digite o valor a ser sacado: "))
                        conta.sacar(valor)

                    elif opcao == "3":
                        conta.consultar_saldo()

                    elif opcao == "4":
                        conta_destino = int(input("Digite o número da conta de destino: "))
                        valor = float(input("Digite o valor a ser transferido: "))
                        for outra_conta in banco.contas:
                            if outra_conta.numero == conta_destino:
                                conta.transferir(outra_conta, valor)
                                break
                        else:
                            print(f'Conta {conta_destino} não encontrada.')

                    elif opcao == "0":
                        break

                    else:
                        print("Opção inválida. Tente novamente.")

        else:
            print(f'Conta {numero_conta} não encontrada.')

    elif escolha == "5":
        nome_cliente = input("Digite o nome do cliente para consultar: ")
        banco.consultar_cliente(nome_cliente)

    elif escolha == "6":
        numero_conta = int(input("Digite o número da conta para extrato: "))
        banco.extrato_conta(numero_conta)

    elif escolha == "0":
        break

    else:
        print("Opção inválida. Tente novamente.")