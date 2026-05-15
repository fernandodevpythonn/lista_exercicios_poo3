class Usuario:
    def __init__(self,nome = "sem nome", email = "sem email"):
        self.nome = nome
        self.email = email

    def exibir_info(self):
        print(f"nome: {self.nome}, email: {self.email}")
        
    @classmethod
    def criar_usuario_teste(cls):
        print("usuário de teste criado com sucesso")
        return cls("usuario teste","usuario@gmail.com")

usuarios_registrados = []

def executar_metodo():
    usuario_teste = Usuario.criar_usuario_teste()
    usuarios_registrados.append(usuario_teste)
    print(usuarios_registrados)
    print("\nexibindo os dados do usuario")
    usuario_teste.exibir_info()
