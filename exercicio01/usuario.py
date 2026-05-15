class Usuario:
    def __init__(self,nome = "sem nome",email = "sem email"):
        self.nome = nome
        self.email = email
    def email_boas_vindas(self):
        print(f"email enviado para {self.email}...")
        print(f"seja bem vindo(a) {self.nome}")
    def cadastrar_usuario(self):
        self.nome = input("nome: ")
        self.email = input("email: ")

def exibir_info():
    usuario = Usuario("", "")
    usuario.email_boas_vindas()
exibir_info()