from utils import *

def menu():
    print("1 - Exercicio01")
    print("2 - Exercicio02")
    print("3 - Exercicio03")
    print("4 - Exercicio04")
    print("5 - Exercicio05")
    print("6 - Exercicio06")
    
def main():
    while True:
        menu()
        opc = input("escolha uma opção: ")
        match opc:
            case "1":
                main01()
            case "2":
                main02()
            case "3":
                main03()
            case "4":
                main04()
            case "5":
                main05()
            case "6":
                main06()

