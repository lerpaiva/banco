
class Banco:
    def __init__(self):
        self._clientes = []
    
    def adicionar_cliente(self, nome,cpf,idade,telefone,email,senha,saldo):
        cliente = Cliente(nome,cpf,idade,telefone,email,senha,saldo)
        self._clientes.append(cliente)
    
        
    def validar_cliente_por_cpf_e_senha(self,cpf, senha):
        for cliente in self._clientes:
            if cliente.getCPF() == cpf and cliente.getSenha() == senha:
                return cliente
        return None
        
    def excluir_conta(self,cliente):
        self._clientes.pop(cliente)
        print("Cliente excluído com sucesso.")

    def setNome (self, nome):
        self._nome = nome

    def getNome (self):
        return self._nome 

    def setTelefone (self, telefone):
        self._telefone = telefone
    
    def getTelefone (self):
        return self._telefone 

    def setCPF(self, cpf):
        self._cpf = cpf
    
    def getCPF(self):
        return self._cpf 
    
    def getSenha(self):
        return self._senha

    def setSenha(self, senha):
        self._senha = senha
    
    def setEmail(self, email):
        self._email = email
    
    def getEmail(self):
        return self._email
    
    def setIdade(self, idade):
        self._idade = idade
    
    def getIdade(self):
        return self._idade

    def setEndereço(self, endereço):
        self.endereço = endereço
    
    def getEndereço(self):
        return self.endereço
    
    def getClienteCpf(self, cpf):
        for cliente in self._clientes:
            if cliente.getCPF() == cpf:
                return cliente
        return None
    

    
class Cliente:
    def __init__(self, nome,cpf,idade,tel, email, senha, saldo = 0):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
        self._telefone = tel
        self._email = email
        self._senha = senha
        self._saldo = saldo
    def getCPF(self):
        return self._cpf 
    
    def getSenha(self):
        return self._senha

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"R${valor} sacados com sucesso!")
        else:
            print(f'o valor de {valor} passou o limite para saque')


    def depositar (self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}") 

    def getSaldo(self):
        print(f"Seu saldo é de R$ {self._saldo}")

    def transferencia(self, valor, receptor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            receptor.depositar(valor)
            print(f"Transferência concluída, no valor de R${valor}, para o cliente {receptor.getNome()}")
        else:
            print("Transferência inválida")
            
        