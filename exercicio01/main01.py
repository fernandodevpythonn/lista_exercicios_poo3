from .usuario import Usuario
usu = Usuario()

def menu():
    print("==MENU==")
    print("1 - adicionar usuário")
    print("0 - Fechar sistema")
def main01():
    while True:
        menu()
        opc = input("escolha uma opção: ")
        match opc:
            case "1":
                usu.cadastrar_usuario()
                usu.email_boas_vindas()
                break
            case "0":
                print("sistema fechado")
                break
            case _:
                print("valor inválido")
                break