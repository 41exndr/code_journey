def Isograma(palabra):
    palabra = input("¿Qué palabra vamos a evaluar?\n")
    
    palabra_limpia = palabra.lower()
    
    #con set en teoría debería funcionar porque guarda únicamente carácteres únicos
    
    if len(palabra_limpia) == len(set(palabra_limpia)):
        print(f"La palabra {palabra} es un Isograma.")
    else:
        print(f"La palabra {palabra} no es un Isograma.")
        
Isograma("")