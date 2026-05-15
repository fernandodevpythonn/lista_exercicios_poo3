class Usuario:
    def __init__(self, nome,email):
        self.nome = nome
        self.email = email
    def enviar_email(self):
        print(f"seja bem vindo {self.nome}, seu email é {self.email}")
def exibir_info():
    usuario = Usuario("vitor","vitor@gmail.com")
    usuario.enviar_email()

def main04():
    exibir_info()
main04()
