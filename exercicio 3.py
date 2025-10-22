# Definindo a classe Cliente
class Cliente:
    def __init__(self, nome, cpf, endereco):
        
        self.nome = nome      
        self.cpf = cpf        
        self.endereco = endereco  

    # Método para retornar informações do cliente
    def get_informacoes(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"


# Definindo a classe Conta_Corrente que herda de Cliente
class Conta_Corrente(Cliente):
    def __init__(self, nome, cpf, endereco, saldo_inicial=0):
        super().__init__(nome, cpf, endereco)  
        self.__saldo = saldo_inicial  

    # Método para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo.")

    # Método para sacar dinheiro
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido!")
        elif valor > self.__saldo:
            print("Saldo insuficiente! Não é possível sacar além do saldo.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")

    # Método para consultar saldo
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

    # Método para consultar informações do cliente
    def consultar_informacoes(self):
        return self.get_informacoes()
    
    # Método para alterar as informações do cliente
    def alterar_informacoes(self, novo_nome=None, novo_endereco=None):
        if novo_nome:
            self.nome = novo_nome
        if novo_endereco:
            self.endereco = novo_endereco
        print("Informações do cliente atualizadas com sucesso!")


# Criando uma instância da classe Conta_Corrente
conta = Conta_Corrente("Leona Lamounier", "147.167.787-05", "Rua Albuquerque, 567")

# Testando os métodos
conta.consultar_informacoes()
conta.consultar_saldo()
conta.depositar(5000)
conta.sacar(1500)
conta.sacar(8000)  
conta.alterar_informacoes(novo_nome="Leona Monteiro", novo_endereco="Av. Niemeyer, 89")
conta.consultar_informacoes()
conta.consultar_saldo()