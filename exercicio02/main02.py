from .usuario import Usuario
usu = Usuario()

def menu():
    print("==MENU==")
    print("1 - cadastrar usuario teste")
    print("0 - Fechar sistema")
def main02():
    while True:
        menu()
        opc = input("escolha uma opção:")
        match opc:
            case "1":
                usu.criar_usuario_teste()
                break
            case "0":
                print("Sistema fechado")
                break
            case _:
                print("valor inválido")
                break