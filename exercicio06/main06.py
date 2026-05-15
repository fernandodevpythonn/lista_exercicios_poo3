from .usuario import Usuario
usu = Usuario()
def menu():
    print("==MENU==")
    print("1 - criar usuário teste")
    print("2 - validar um email")
    print("3 - criar usuário")
    print("4 - Fechar sistema")
def main06():
    while True:
        menu()
        opc = input("escolha uma opção: ")
        match opc:
            case "1":
               usu.criar_usuario_teste()
               break
            case "2":
               usu.criar_email()
               break
            case "3":
                usu.inserir_usuario()
                break
            case "4":
                print("sistema encerrado")
                break
            case _:
                print("Valor inválido")
                break
