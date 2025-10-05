def tiene_cero(numero):
    """Verifica si el número contiene el dígito 0"""
    return "0" in str(numero)

def suma_pares(numero):
    """Calcula la suma de los dígitos pares"""
    suma = 0
    for digito in str(numero):
        if int(digito) % 2 == 0:
            suma += int(digito)
    return suma

def suma_impares(numero):
    """Calcula la suma de los dígitos impares"""
    suma = 0
    for digito in str(numero):
        if int(digito) % 2 != 0:
            suma += int(digito)
    return suma

def main():
    """Función principal del programa"""
    while True:
        try:
            entrada = input("¿Qué número vas a evaluar? (0 para salir): ")
            numero = int(entrada)
            
            if numero == 0:
                print("Saliendo del programa...")
                break
            
            if numero < 0:
                print("Por favor, ingresa un número positivo.")
                continue
            
            # Verificar condiciones y mostrar resultado
            if not tiene_cero(numero):
                if suma_pares(numero) > suma_impares(numero):
                    print(1)
                else:
                    print(0)
            else:
                print("El número contiene el dígito 0, no se evalúa.")
                
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()