from .usuario import Usuario
usu = Usuario()

def menu():
    print("1 - adicionar usuário")
def main01():
    while True:
        menu()
        opc = input("escolha uma opção: ")
        match opc:
            case "1":
                usu.cadastrar_usuario()
                usu.email_boas_vindas()

