from .usuario import Usuario
usu = Usuario()
def menu():
    print("1 - criar usuário teste")
    print("2 - validar um email")
    print("3 - criar usuário")
    print("4 - Sair")
def main06():
    while True:
        menu()
        opc = input("escolha uma opção: ")
        match opc:
            case "1":
                usu.criar_usuario_teste()
            case "2":
               usu.criar_email()
            case "3":
                usu.inserir_usuario()
            case "4":
                print("sistema encerrado")
                break
            case _:
                print("Valor inválido")
                break
