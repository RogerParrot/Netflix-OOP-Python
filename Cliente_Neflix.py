class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ["basic", "premium"]
        self.plano = plano
    
cliente1 = Cliente("Rogerio", "rogerio@gmail.com", "basic")
print(cliente1.nome)
print(cliente1.email)
print(cliente1.plano)