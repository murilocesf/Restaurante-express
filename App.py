import os

#restaurantes = ["Pé de banha", "Coritiba feijoadas"]
#Inserir dicionario em outra linguagem, chave valor
restaurante=[{}]

def finalizar_app():
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")
   
def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def mostrar_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()
   


def escolher_opcoes():
    mostrar_subtitulo("Programa Expresso\n")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def opcao_invalida():
    mostrar_subtitulo("Opção inválida\n")
    voltar_menu_principal()

def chamar_nome_do_app():
    print("Restaurante Expressao\n")

def listarRestaurantes():
   
    mostrar_subtitulo('Listando os Restaurantes')
    for restaurante in restaurantes:
        print(f'-{restaurantes}')
        voltar_menu_principal()
       

def cadastrar_novo_restaurante():
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")
    voltar_menu_principal()
   

def main():
    escolher_opcoes()
    chamar_nome_do_app()
    try:
        opcaodigitada = int(input("Digite a opção desejada: "))
        if opcaodigitada == 1:
            print("Você escolheu cadastrar restaurante\n")
            cadastrar_novo_restaurante()
        elif opcaodigitada == 2:
            listarRestaurantes()
        elif opcaodigitada == 3:
            print("Você escolheu ativar restaurante\n")
        elif opcaodigitada == 4:
            print("Você escolheu sair do aplicativo\n")
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

if __name__ == "__main__":
    finalizar_app()
    main()
