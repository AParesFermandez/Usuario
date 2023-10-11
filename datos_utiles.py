# declarar una clase y darle el nombre Usuario
class Usuario:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

Usuario()
guido = Usuario()
monty = Usuario()
# Accediendo a los atributos de la instancia
print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael

guido.name = "Guido"
print(guido.name) # salida: Guido
monty.name = "Monty"
print(monty.name) # salida: Monty

class User:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

guido = Usuario()
monty = Usuario()
guido.nombre_banco = "Dojo Credit Union"
print(guido.bank_name) # salida: Dojo Credit Union 
print(monty.bank_name) # salida: Primer Dojo Nacional

User.bank_name = "Banco del Dojo"
print(guido.nombre_banco) # salida: Banco del Dojo
print(monty.nombre_banco) # salida: Banco del Dojo


class Usuario:

# los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
# ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python

guido.hacer_depósito(100)

class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido

guido.hacer_depósito(100)
guido.hacer_depósito(200)
monty.hacer_depósito(50)
print(guido.balance_cuenta)	# salida: 300
print(monty.balance_cuenta)	# salida: 50




