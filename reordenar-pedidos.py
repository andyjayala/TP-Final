from datos import lista_pedidos_1000, lista_pedidos_10000, lista_pedidos_100000
from funciones import invertir_orden_reversed, invertir_con_bucle, invertir_orden_slicing, medir_tiempo_y_memoria

# Parte 3: Invertir la lista de pedidos
# Problema: Clara quiere armar los paquetes en orden inverso al que fueron pedidos (para que el último pedido salga primero).
# Objetivo: Invertir la lista de pedidos.


# Creamos un grupo de datos definidos por la cantidad de elementos, por cada uno hay: lista, conjunto, etiqueta
grupos_de_datos = [
    (lista_pedidos_1000, "1000"),
    (lista_pedidos_10000, "10000"),
    (lista_pedidos_100000, "100000")
]

# Recorremos cada elemento (lista y etiqueta) del grupo de datos
for lista_pedidos, etiqueta in grupos_de_datos:
    # Medimos la lista de cada uno de los grupos de datos
    resultado_lista, tiempo_lista, memoria_actual_lista, memoria_maxima_lista = medir_tiempo_y_memoria(invertir_orden_reversed, lista_pedidos)
    print(f"El reordenamiento con reveresed de una lista con {etiqueta} elementos conlleva: {tiempo_lista:.6f} seg, pico de memoria: {memoria_maxima_lista} bytes")

    resultado_lista, tiempo_lista, memoria_actual_lista, memoria_maxima_lista = medir_tiempo_y_memoria(invertir_con_bucle, lista_pedidos)
    print(f"El reordenamiento con bucle de una lista con {etiqueta} elementos conlleva: {tiempo_lista:.6f} seg, pico de memoria: {memoria_maxima_lista} bytes")

    resultado_lista, tiempo_lista, memoria_actual_lista, memoria_maxima_lista = medir_tiempo_y_memoria(invertir_orden_slicing, lista_pedidos)
    print(f"El reordenamiento con slicing de una lista con {etiqueta} elementos conlleva: {tiempo_lista:.6f} seg, pico de memoria: {memoria_maxima_lista} bytes")

    print("_" * 40)