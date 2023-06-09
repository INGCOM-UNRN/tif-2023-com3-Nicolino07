

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def solo_float(entrada):
    while (entrada):
        try:
            numero = float(entrada)
        except:
            entrada = input("ingrese un número\n")
        else:
            entrada = False 
    entrada = numero        
    return float(entrada)


def dividir(a, b):
    while b == 0:
        print("No se puede dividir entre cero.")
        b = input("Ingrese otro número\n")
        b = solo_float(b)

    return a / b    
    
# Solicitar el primer valor al usuario

valor1 = input("Ingrese el primer valor:\n ")
resultado = solo_float(valor1) 
salida = False

while salida is False:
    operador = input("Ingrese el operador (+, -, *, /) o '=' para obtener el resultado: \n")

    if operador == '=':
        salida = True
    else:


        if operador == '+':
            valor2 = input("Ingrese el siguiente valor: \n")
            valor2 = solo_float(valor2) 
            resultado = sumar(resultado, valor2)
        elif operador == '-':
            valor2 = input("Ingrese el siguiente valor: \n")
            valor2 = solo_float(valor2) 
            resultado = restar(resultado, valor2)
        elif operador == '*':
            valor2 = input("Ingrese el siguiente valor: \n")
            valor2 = solo_float(valor2) 
            resultado = multiplicar(resultado, valor2)
        elif operador == '/':
            valor2 = input("Ingrese el siguiente valor: \n")
            valor2 = solo_float(valor2)   
            resultado = dividir(resultado, valor2)
        else:
            print("Operador inválido.")

# Mostrar el resultado final
print("El resultado es:\n", resultado)