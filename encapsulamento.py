import os

os.system("cls || clear") #Limpar teminal

#Definição classes

#criando exceção.
class SaldoInsuficienteError(Exception):
    pass
class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 #Atributo protegido

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        #try - except
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"
        self._saldo -= valor
        return self._saldo
    
    def __verificar_sacar(self, valor): #Metodo privado.
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.") #Lancamento de erro.
        
    def depositar(self, valor):
        try:
                self.__verificar_depositar(valor)
        except ValorNegativoError as error:
            return f"Error: {error}"

        self._saldo += valor
        return self._saldo

    def __verificar_depositar(self, valor):
        if valor < 0:
            raise ValorNegativoError("Não é possivel depositar valor negativo.") 

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciando classes.
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

print(conta_corrente.saldo)

print(conta_corrente.sacar(200))

print(conta_corrente.saldo)

print(conta_corrente.depositar(-200))