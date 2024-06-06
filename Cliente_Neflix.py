class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ["basic", "premium"]
        self.plano = plano
    
    def mudarPlano(self, plano):
        if plano in self.planos:
            self.plano = plano
            print(f'Novo plano: {plano}')
        else:
            print("Plano inválido!")

    def mudarNomeUsuario(self, outroNome):
        self.nome = outroNome
        print(f'Nome de usuário alterado para: {outroNome}')

cliente1 = Cliente("Rogério", "rogerio@gmail.com", "basic")
print(cliente1.nome)
print(cliente1.email)
print(cliente1.plano)

cliente1.mudarPlano("premium")

cliente1.mudarNomeUsuario("RogerParrot")