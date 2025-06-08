from datos import lista_clientes_1000, lista_clientes_10000, lista_clientes_100000,conjunto_clientes_1000, conjunto_clientes_10000, conjunto_clientes_100000
from funciones import buscar_en_lista, buscar_en_conjunto, medir_tiempo_y_memoria

# Parte 1: Buscar si un cliente hizo un pedido
# Problema: Tiene una lista de nombres de clientes que hicieron pedidos hoy.
# Objetivo: Saber si nombre está en la lista.
nombre = "Lucía Fernández"

# Creamos un grupo de datos definidos por la cantidad de elementos, por cada uno hay: lista, conjunto, etiqueta
grupos_de_datos = [
    (lista_clientes_1000, conjunto_clientes_1000, "1000"),
    (lista_clientes_10000, conjunto_clientes_10000, "10000"),
    (lista_clientes_100000, conjunto_clientes_100000, "100000")
]

# Recorremos cada elemento (lista, conjunto, etiqueta) del grupo de datos
for lista_clientes, conjunto_clientes, etiqueta in grupos_de_datos:
    # Medimos la lista de cada uno de los grupos de datos
    resultado_lista, tiempo_lista, memoria_actual_lista, memoria_maxima_lista = medir_tiempo_y_memoria(buscar_en_lista, nombre, lista_clientes)
    print(f"{nombre} {'está' if resultado_lista else 'no está'} en la lista de {etiqueta}")
    print(f"Búsqueda con lista de {etiqueta}: {tiempo_lista:.6f} seg, pico de memoria: {memoria_maxima_lista} bytes")

    # Medimos los conjuntos de cada uno de los grupos de datos
    resultado_conjunto, tiempo_conjunto, memoria_actual_conjunto, memoria_maxima_conjunto = medir_tiempo_y_memoria(buscar_en_conjunto, nombre, conjunto_clientes)
    print(f"{nombre} {'está' if resultado_conjunto else 'no está'} en el conjunto de {etiqueta}")
    print(f"Búsqueda con conjunto de {etiqueta}: {tiempo_conjunto:.6f} seg, pico de memoria: {memoria_maxima_conjunto} bytes")

    print("_" * 40)
