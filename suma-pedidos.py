from datos import lista_cantidad_productos_100, lista_cantidad_productos_1000, lista_cantidad_productos_10000, lista_cantidad_productos_100000
from funciones import suma_bucle, suma_con_recursividad, suma_con_sum,  medir_tiempo_y_memoria

# Parte 2: Calcular la suma de productos vendidos
# Problema: Cada pedido tiene una cantidad de productos. Queremos saber cuántos productos se vendieron en total.
# Objetivo: Sumar todas las cantidades.

# Creamos un grupo de datos definidos por la cantidad de elementos, por cada uno hay: lista, conjunto, etiqueta
grupos_de_datos = [
    (lista_cantidad_productos_100, "100"),
    (lista_cantidad_productos_1000, "1000"),
    (lista_cantidad_productos_10000, "10000"),
    (lista_cantidad_productos_100000, "100000")
]

# Recorremos cada elemento (lista, conjunto, etiqueta) del grupo de datos
for lista_cantidad_productos, etiqueta in grupos_de_datos:
    # Medimos la lista de cada uno de los grupos de datos
    resultado_funcion, tiempo_lista, memoria_actual_lista, memoria_maxima_lista = medir_tiempo_y_memoria(suma_bucle, lista_cantidad_productos)
    print(f"El resultado de la suma con bucle es: {resultado_funcion}")
    print(f"Las medidas con {etiqueta} elementos: {tiempo_lista:.6f} seg, pico de memoria: {memoria_maxima_lista} bytes")

    resultado_funcion, tiempo_lista, memoria_actual_lista, memoria_maxima_lista = medir_tiempo_y_memoria(suma_con_sum, lista_cantidad_productos)
    print(f"El resultado de la suma con sum es: {resultado_funcion}")
    print(f"Las medidas con {etiqueta} elementos: {tiempo_lista:.6f} seg, pico de memoria: {memoria_maxima_lista} bytes")

    #La suma con recursividad la podemos hacer solo con esta cantidad, ya que con más obtenemos el error de sobrecarga de pila
    if(etiqueta == "100"):
        resultado_funcion, tiempo_lista, memoria_actual_lista, memoria_maxima_lista = medir_tiempo_y_memoria(suma_con_recursividad, lista_cantidad_productos)
        print(f"El resultado de la suma con recursividad es: {resultado_funcion}")
        print(f"Las medidas con {etiqueta} elementos: {tiempo_lista:.6f} seg, pico de memoria: {memoria_maxima_lista} bytes")

    print("_" * 40)
