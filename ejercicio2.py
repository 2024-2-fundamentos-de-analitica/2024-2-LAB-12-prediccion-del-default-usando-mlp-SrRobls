"""
 Tiempo restante 4:48:53
Pregunta 2
Sin finalizar
Se puntúa como 0 sobre 1,6
Marcar pregunta
Enunciado de la pregunta

Procedimiento: Elabore un algoritmo e impleméntelo en Python que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura con la opción <1>, pagar una existente mediante la opción <2> o terminar con la opción <0>. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro. 


Instrucciones:

Entradas: Para este ejercicio permita ingresar las variables de entrada mediante la instrucción “input”, sin comentarios de entrada, en el estricto orden que aparece abajo.  

 
1.    opcion:  Menú de opciones.                                      --> Int type
2.    numero: ingreso del número factura.                        --> Int type
3.    valor: Precio de la factura.                                          --> Int type
4.    opcion: Número de factura a pagar. (opcional)         --> entran en el mismo input
5.    opcion: Comando de terminación de operación.      --> entran en el mismo input


Salidas: Permita que se genere las salidas mediante el comando “print” en el estricto orden que aparece abajo y evitando imprimir comentarios. Es decir, imprima solo el dato de salida.

1.    output1:  Cantidad cobrada hasta el momento.                          --> Int type
2.    output1: Cantidad pendiente por cobrar.                                    --> Int type
"""

facturas = {}
pagado = 0
pendiente = 0
while True:
    opcion = int(input()) # 0: terminar, 1: añadir factura, 2: pagar factura
    if opcion == 0: # terminar
        break
    elif opcion == 1: # añadir factura
        numero = int(input())
        valor = int(input())
        facturas[numero] = valor
        pendiente += valor
    elif opcion == 2: # pagar factura
        numero = int(input())
        pagado += facturas[numero]
        pendiente -= facturas[numero]
        facturas.pop(numero)

    print(pagado)
    print(pendiente)
        
