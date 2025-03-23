productos = int(input("¿ Cuantos productos va a comprar ?: "))  #Cremoa suna variable para saber cuantos productos se ingresaran

cont = 0  #Declaramos con en 0
suma = 0  #Declaramos suma en cero
while cont < productos:   #El bucle while se reptira miestras cont sea menor a los porductos que decidimos ingresar
        valor = float(input("Ingrese el valor: "))  #Ingresamos los valores
        suma = suma + valor  #Sumamos los valores
        cont = cont + 1  #Contamos uno en cada reptición


descuento_f = int(input("Ingrese el descuento: "))  #Creamos una variable la cual nos va indicar el descuento




def calcular_descuento (monto,descuento): #Creamos la función con 2 parametros monto y descuento

    des = monto -  (monto * descuento / 100)  # Calculamos el descuento restando el porcentaje menos el monto
    return f"El monto total es de {suma},el descuento es del {descuento_f}% y el valor total a pagar es de $ {des} dolares"  #Retornamos un mensaje


de = calcular_descuento(suma,descuento_f)  #Llamamos a nuestra función y le pasamos los parametros
print(de)  #Imprimimos la función