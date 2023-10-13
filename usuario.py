class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_depósito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount):
        if amount <= self.balance_cuenta:
            self.balance_cuenta -= amount
        else:
            print("Fondos insuficientes para el retiro.")
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")
        return self

    def transferir_dinero(self, other_user, amount):
        if amount <= self.balance_cuenta:
            self.hacer_retiro(amount)
            other_user.hacer_depósito(amount)
            print(f"{self.name} ha transferido ${amount} a {other_user.name}")
        else:
            print("Fondos insuficientes para la transferencia.")
        return self

# Crear 3 instancias de la clase Usuario
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
tercer_usuario = Usuario("Tercer Usuario", "tercer@usuario.com")

# Realizar transacciones con los usuarios
guido.hacer_depósito(100).hacer_depósito(50).hacer_depósito(200).hacer_retiro(75)
monty.hacer_depósito(200).hacer_depósito(150).hacer_retiro(50).hacer_retiro(75)
tercer_usuario.hacer_depósito(300).hacer_retiro(50).hacer_retiro(25).hacer_retiro(75)

# Mostrar los balances de los usuarios
guido.mostrar_balance_usuario()
monty.mostrar_balance_usuario()
tercer_usuario.mostrar_balance_usuario()

# Realizar una transferencia
guido.transferir_dinero(tercer_usuario, 50)

# Mostrar los balances después de la transferencia
guido.mostrar_balance_usuario()
tercer_usuario.mostrar_balance_usuario()
