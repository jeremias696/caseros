import random

def generate_password():
    mayusculas = ['A','B','C','E','D']
    minusculas = ['a','b','c','d','e']
    simbolos = ['€','#','&','!','/','@']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    caracteres = mayusculas + minusculas+simbolos+numeros
    contrasena = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena)
    return contrasena

def run():    
    contrasena = generate_password()
    print('la nueva contraseña es : ' + contrasena)
if __name__ == '__main__':
    run()