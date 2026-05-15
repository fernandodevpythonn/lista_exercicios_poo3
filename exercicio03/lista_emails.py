
class Usuario:
    def __init__(self, nome = "sem nome", email = "sem email"):
        if not Usuario.validar_email(email):
            raise ValueError("email inválido")
        self.nome = nome
        self.email = email
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email

def executar_metodo():
    print("validando emails")
    emails = ["fernando@gmail.com", "usuário-sem-arroba.com", "teste@gmail"]

    for e in emails:
        valido = Usuario.validar_email(e)
        print(f"{e}: {'valido' if valido else 'invalido'}")

def main03():
    executar_metodo()
main03()