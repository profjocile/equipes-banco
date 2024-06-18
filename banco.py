"""
Esta classe representa um banco, com funcionalidades básicas de depósito e saque.
O saldo da conta é mantido internamente e pode ser acessado através da propriedade 'saldo'.
Caso o valor do saque seja maior que o saldo disponível, uma exceção será lançada.
"""
class Banco:
    def __init__(self):
        self._saldo = 0
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        if valor > self._saldo:
            print('Saldo insuficiente')             
        self._saldo -= valor

cliente = Banco()
cliente.depositar(1000)
print(cliente.saldo)
cliente.sacar(1000)
print(cliente.saldo)