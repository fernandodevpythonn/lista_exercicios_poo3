class Usuario:
    def __init__(self,nome,email):
        if not Usuario.validar_email(email):
            raise ValueError("erro: email inválido")
        self.nome = nome
        self.email = email

    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email

def cadastrar_usuario():
    nome = input("digite seu nome: ")
    email = input("digite seu email: ")
    usuario = Usuario(nome,email)
    print(f"Usuário {usuario.nome}, com o email {usuario.email}, cadastrado")

def main05():
    cadastrar_usuario()

main05()