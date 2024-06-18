"""
Esta classe representa um banco, com funcionalidades básicas de depósito e saque.
O saldo da conta é mantido internamente e pode ser acessado através da propriedade 'saldo'.
Caso o valor do saque seja maior que o saldo disponível, uma exceção será lançada.
"""
from datetime import datetime


class Banco:
    def __init__(self):
        self._saldo = 0
        self._extrato = []
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def extrato(self):
        return f'Extrato: {self._extrato}\n Saldo: {self._saldo}'

    def depositar(self, valor):
        self._saldo += valor
        self._extrato.append(
            {
                "tipo":'deposito',
                "valor": valor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        print(f'Deposito de R$ {valor} realizado com sucesso!')

    def sacar(self, valor):
        if valor > self._saldo:
            print('Saldo insuficiente')             
        else:
            self._saldo -= valor
            self._extrato.append(
                {
                    "tipo":'-saque--',
                    "valor": valor,
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            print(f'Saque de R$ {valor} realizado com sucesso!')

    def __str__(self):
        return f'Saldo: {self._saldo}'
    
    def mostrar_extrato(self):
        for item in self._extrato:
            print(f'{item["data"]}\t{item["tipo"]}\tR$ {item["valor"]}')
        print('=' * 20)
        print(f'Saldo: {self._saldo}')

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(menu)

def main():
    cliente = Banco()
    while True:
        opcao = menu()
        if opcao == 'd':
            valor = int(input('Digite o valor: '))
            cliente.depositar(valor)
        elif opcao == 's':
            valor = int(input('Digite o valor: '))
            cliente.sacar(valor)
        elif opcao == 'e':
            cliente.mostrar_extrato()
        elif opcao == 'q':
            break

if __name__ == '__main__':
    print('Bem-vindo ao Banco App')
    print('=' * 20)    
    main()