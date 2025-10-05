class Checker:
    def __init__(self, numero):
        self.numero_casos = numero
        self.lista = []
    
    def pedir_nums(self):
        for i in range(self.numero_casos):
            num = int(input(f"Ingrese el número {i+1} a evaluar: "))
            self.lista.append(num)
    
    def verificar_primos(self):
        for num in self.lista:
            if num < 2:
                print(f"{num} no es primo ni compuesto")
                continue
                
            es_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            
            if es_primo:
                print(f"{num} es primo.")
            else:
                print(f"{num} es compuesto.")

check = Checker(int(input("¿Cuántos números vas a evaluar? ")))
check.pedir_nums()
check.verificar_primos()
