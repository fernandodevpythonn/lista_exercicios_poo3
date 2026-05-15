from utils import *

def menu():
    print("====MENU LISTAS DE EXERCÍCIOS====")
    print("1 - Exercicio01")
    print("2 - Exercicio02")
    print("3 - Exercicio03")
    print("4 - Exercicio04")
    print("5 - Exercicio05")
    print("6 - Exercicio06")
    print("0 - Fechar sistema")
    
def main():
  while True:
    menu()
    opc = input("escolha um exercício: ")
    match opc:
        case "1":
            main01()
            input("aperte Enter para voltar")
        case "2":
            main02()
            input("aperte Enter para voltar")
        case "3":
            main03()
            input("aperte Enter para voltar")
        case "4":
            main04()
            input("aperte Enter para voltar")
        case "5":
            main05()
            input("aperte Enter para voltar")
        case "6":
            main06()
            input("aperte Enter para voltar")
        case "0":
            print("Sistema fechado")
            break
        case _:
            print("valor inválido")
            break

if __name__ == "__main__":
    main()