class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Insira um valor positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor de saque inválido. Insira um valor positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta = ContaBancaria("João", 1000)

# Exibindo o saldo inicial
conta.exibir_saldo()

# Realizando um depósito e exibindo o saldo
conta.depositar(200)
conta.exibir_saldo()

# Realizando um saque e exibindo o saldo
conta.sacar(500)
conta.exibir_saldo()

# Tentativa de saque com saldo insuficiente
conta.sacar(1000)
conta.exibir_saldo()