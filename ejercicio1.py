"""
Procedimiento:  Realice un algoritmo que contenga una función la cual determine si un número real ingresado por consola es primo o no, si es primo debe mostrar el mensaje sin comillas ni tildes: “El numero es primo”, si el número no lo es debe mostrar el mensaje “El numero no es primo”.
Recuerde que los números primos solo pueden ser cantidades enteras positivas, por lo cual la función deberá tener la validación en el caso en el que se ingrese una cantidad negativa, en cuyo caso se deberá mostrar el mensaje sin comillas ni tildes: “No positivo”. Además, si no es entero, pero si positivo el programa debe mostrar el mensaje sin comillas ni tildes: “No entero”.

Instrucciones:

Entradas: Para este ejercicio permita ingresar las variables de entrada mediante la instrucción “input”, sin comentarios de entrada, en el estricto orden que aparece abajo. 

 

1.       N:  Número real.

Salidas: Permita que se genere las salidas mediante el comando “print” en el estricto orden que aparece abajo y evitando imprimir comentarios. Es decir, imprima solo el dato de salida. 
"""


n = float(input())
if n < 0:
        print("No positivo")
elif n != int(n):
        print("No es entero")
else:
    if n == 0 or n == 1:
        print("El numero no es primo")
    else:
        for i in range(2, int(n)):
            if n % i == 0:
                print("El numero no es primo")
                break
        else:
            print("El numero es primo")