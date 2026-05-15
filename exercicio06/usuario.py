class Usuario:
    def __init__(self, nome = "sem nome", email = "sem email"):
        self.nome = nome
        self.email = email
    
    @classmethod
    def criar_usuario_teste(cls):
        print("usuário teste criado com sucesso")
        return cls("Usuario teste", "Usuarioteste@gmail.com")
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
    def criar_email(self):
        self.email = input("Inserir email: ")
        if not Usuario.validar_email(self.email):
            raise ValueError("erro: email inválido")
        else:
            print("email válido")

    def inserir_usuario(self):
        self.nome = input("digite seu nome: ")
        self.email = input("digite seu email: ")
        if not Usuario.validar_email(self.email):
            raise ValueError("erro: email inválido")
        print(f"usuário {self.nome}, com o email {self.email} cadastrado")
    