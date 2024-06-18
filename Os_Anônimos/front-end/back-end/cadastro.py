from flask import Flask

app = Flask(__name__)

print(app)







@app.route('/')
def index(html):
    return app

if __name__ == '__main__':
    app.run(debug=True)





def main():
    while True:
        print(menu)
        opção = input('Insira sua escolha: ')
        if opção == '+':
            cadastrar_Aluno()
        elif opção == 'M':
            print(lista_nome)
        elif opção == 'G':
            gravar_nomes()
        elif opção == 'Dell':
            exluir_nome()
        else:
            print("Insira uma opção válida! Corno!")
            continue


lista_nome = []

menu = '''
Escolha:
[+] Adicionar um novo Aluno ao Sistema
[X] Sair
[M] Mostrar lista de Alunos
[G] Gravar lista de alunos em arquivo .txt
[Dell] Deleta um nome específico'''

if __name__ == '__main__':
    main()