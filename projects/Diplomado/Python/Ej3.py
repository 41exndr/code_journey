archivo1 = open("matrices.txt", "r")
archivo2 = open("salida.txt", "w")

numero = int(archivo1.readline())
numgrande = 0
lista = []

for i in range(numero):
    dimension = int(archivo1.readline())
    for i2 in range(dimension):
        lista = list(archivo1.readline().split())
        for i3 in lista:
            if(int(i3)>numgrande): # acá actualiza i3 con cada número de la lista de cada linea de las matrices
                numgrande = int(i3) # si numero de la matriz es más alto que el anterior registrado, guarda el mas alto.
    archivo2.write(f"número mayor de la matriz {i+1}: {numgrande} \n")
    numgrande = 0 # reinicia el numero mas alto para la proxima matriz, el primer for va el numero de matrices 
    # declarado en la primera linea de matrices.txt (en este caso 2).

archivo1.close()
archivo2.close()
