def Harshad(numero):
    numero = input("¿Qué número vamos a evaluar?\n")

    try:
        checknum = int(numero)
    except ValueError:
        return "Por favor, ingresar un número entero."
    
    if checknum < 0:
        return f"{checknum} no es un número Harshad, debe ser positivo."
    
    sumanum = 0 # acá se suman los números enteros con una iteración 
    for dig in numero:
        sumanum += int(dig)
    
    if checknum % sumanum == 0:
        return f"¡{checknum} es un número Harshad!\n{numero} dividido por {sumanum} es {checknum // sumanum}. (Residuo 0)."
    else:
        return f"¡No es un número Harshad! no es divisible por {sumanum}."

print(Harshad(""))