from os import system
import Hanoi
import time

def main():
    cantidad_discos = Hanoi.menu()
    Hanoi.inicializar_torres()
    Hanoi.llenar_torres(cantidad_discos)
    Hanoi.crear()
    Hanoi.actualizar_matriz()
    
    pasos = 0
    tiempo_inicio = time.time()
    
    while True:
        system("cls")
        
        Hanoi.mostrartorres(pasos)
        Hanoi.mostrar(Hanoi.l1[1:], Hanoi.l2[1:], Hanoi.l3[1:])
        
        if Hanoi.ganar(cantidad_discos):
            tiempo_fin = time.time()
            print('\n¡FELICIDADES! HAS GANADO!')
            print(f'Tiempo: {tiempo_fin - tiempo_inicio:.2f} segundos')
            print(f'Pasos totales: {pasos}')
            
            opcion = input('\nReiniciar <1>   Menu <2>   Salir <3>: ')
            if opcion == '1':
                Hanoi.inicializar_torres()
                Hanoi.llenar_torres(cantidad_discos)
                Hanoi.actualizar_matriz()
                pasos = 0
                tiempo_inicio = time.time()
                
            elif opcion == '2':
                cantidad_discos = Hanoi.menu()
                Hanoi.inicializar_torres()
                Hanoi.llenar_torres(cantidad_discos)
                Hanoi.actualizar_matriz()
                pasos = 0
                tiempo_inicio = time.time()
                
            elif opcion == '3':
                break
            continue
        

        print('\nMovimientos disponibles:')
        print('1-2: Torre 1 → Torre 2')
        print('1-3: Torre 1 → Torre 3') 
        print('2-1: Torre 2 → Torre 1')
        print('2-3: Torre 2 → Torre 3')
        print('3-1: Torre 3 → Torre 1')
        print('3-2: Torre 3 → Torre 2')
        print('4: Reiniciar  5: Menu  6: Salir')
        
        movimiento = input('\nIngresa tu movimiento: ')
        

        if movimiento == '1-2':
            Hanoi.mover1_2()
            pasos += 1
        elif movimiento == '1-3':
            Hanoi.mover1_3()
            pasos += 1
        elif movimiento == '2-1':
            Hanoi.mover2_1()
            pasos += 1
        elif movimiento == '2-3':
            Hanoi.mover2_3()
            pasos += 1
        elif movimiento == '3-1':
            Hanoi.mover3_1()
            pasos += 1
        elif movimiento == '3-2':
            Hanoi.mover3_2()
            pasos += 1
        elif movimiento == '4':

            Hanoi.inicializar_torres()
            Hanoi.llenar_torres(cantidad_discos)
            Hanoi.actualizar_matriz()
            pasos = 0
            tiempo_inicio = time.time()
        elif movimiento == '5':

            cantidad_discos = Hanoi.menu()
            Hanoi.inicializar_torres()
            Hanoi.llenar_torres(cantidad_discos)
            Hanoi.actualizar_matriz()
            pasos = 0
            tiempo_inicio = time.time()
        elif movimiento == '6':

            break
        else:
            print('Movimiento inválido!')
            input('Presiona Enter para continuar...')

if __name__ == "__main__":
    main()