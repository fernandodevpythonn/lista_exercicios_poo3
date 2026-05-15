from .usuario import Usuario
usu = Usuario()

def menu():
    print("1 - cadastrar usuario teste")
def main02():
    while True:
        menu()
        opc = input("escolha uma opção:")
        match opc:
            case "1":
                usu.criar_usuario_teste()

