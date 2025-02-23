"""
Procedimiento: Una matriz diagonal es una matriz cuadrada en la cual todos los elementos situados por encima y por debajo de la diagonal principal son ceros. Los siguientes ejemplos se consideran matrices diagonales:
Como es de esperarse, para que exista una diagonal, la matriz debe ser siempre cuadrada. Es decir, la cantidad de columnas es igual a las filas y simplemente se habla de la dimensión de la matriz en lugar del número de filas y columnas. 
 
Elaborar un algoritmo e impleméntelo en Python que se asegure que la matriz ingresada es cuadrada, de no serlo se imprime por pantalla el mensaje sin comillas ni tildes: “Ingrese una matriz cuadrada” y vulva a pedir el ingreso de la matriz hasta que ingrese una matriz cuadrada. Además, el programa debe analizar y determine si la matriz es diagonal o no, de serlo debe imprime por consola el mensaje si comillas ni tildes: “Matriz diagonal”, de no serlo imprime el mensaje por consola sin comillas ni tilde “No es matriz diagonal”.  
 
Instrucciones:
Entradas: Para este ejercicio permita ingresar las variables de entrada mediante la instrucción “input”, sin comentarios de entrada, en el estricto orden que aparece abajo.  
 

    N: Dimensión de la matriz.
    filas: Ingreso de filas (ingrese con un ciclo). Por ejemplo, para la matriz A:  

    Primera fila:    3,0,0     --> string inpunt
    Segunda fila:  0,5,0     --> string inpunt
    Tercera fila:     0,0,2     --> string inpunt 

Salidas:  Permita que se genere las salidas mediante el comando “print” en el estricto orden que aparece abajo y evitando imprimir comentarios. Es decir, imprima solo el dato de salida. 
 

    output:  mensaje solicitado en la salida.  

Por ejemplo:
Entrada 	Resultado

3
1,2,3
4,5
6,7,8
1,0,0
0,1,0
0,0,1

	

Ingrese una matriz cuadrada
Matriz diagonal
"""

N = int(input()) # Dimensión de la matriz
matriz = [] # Matriz
error = False # Error en la matriz
while True:
    for i in range(N):
        fila = input().split(',') # Ingreso de filas si ingreso 1,2,3,4,5,6,7,8,9 me lo da en una lista ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(fila) != N: # Si la cantidad de elementos de la fila no es igual a la dimensión de la matriz
            error = True
        matriz.append(fila)
    if error: # Si hay un error en la matriz
        print("Ingrese una matriz cuadrada")
        matriz = [] # Reinicio la matriz
        error = False # Reinicio el error
    else:
        break
    


for i in range(N):
    for j in range(N):
        
        if i != j and matriz[i][j] != '0':
            print("No es matriz diagonal")
            break
    else:
        continue
    break
else:
    print("Matriz diagonal")
        