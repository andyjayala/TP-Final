import time
from datos import lista_clientes_1000, conjunto_clientes_1000, lista_cantidad_productos_100, lista_pedidos_1000
from funciones import buscar_en_lista, buscar_en_conjunto, suma_bucle, suma_con_recursividad, suma_con_sum, invertir_con_bucle, invertir_orden_reversed, invertir_orden_slicing

# Parte 1: Buscar si un cliente hizo un pedido
# Problema: Tiene una lista de nombres de clientes que hicieron pedidos hoy.
# Objetivo: Saber si nombre está en la lista.
nombre = "Andrea Castro" 

empieza_busqueda_con_bucle = time.time()
en_lista = buscar_en_lista(nombre, lista_clientes_1000)
termina_busqueda_con_bucle = time.time()
empieza_busqueda_con_conjunto = time.time()
en_conjunto = buscar_en_conjunto(nombre, conjunto_clientes_1000)
termina_busqueda_con_conjunto = time.time()

tiempo_lista = termina_busqueda_con_bucle - empieza_busqueda_con_bucle
tiempo_conjunto = termina_busqueda_con_conjunto - empieza_busqueda_con_conjunto

print(f"¿'{nombre}' está en la lista? {'Sí' if en_lista else 'No'} - Tiempo: {tiempo_lista:.6f} segundos")
print(f"¿'{nombre}' está en el conjunto? {'Sí' if en_conjunto else 'No'} - Tiempo: {tiempo_conjunto:.6f} segundos")

# Parte 2: Calcular la suma de productos vendidos
# Problema: Cada pedido tiene una cantidad de productos. Queremos saber cuántos productos se vendieron en total.
# Objetivo: Sumar todas las cantidades.

empieza_bucle = time.time()
resultado_bucle = suma_bucle(lista_cantidad_productos_100)
termina_bucle = time.time()
tiempo_bucle = termina_bucle - empieza_bucle

empieza_sum = time.time()
resultado_sum = suma_con_sum(lista_cantidad_productos_100)
termina_sum = time.time()
tiempo_sum = termina_sum - empieza_sum

empieza_recursiva = time.time()
resultado_recursiva = suma_con_recursividad(lista_cantidad_productos_100)
termina_recursiva = time.time()
tiempo_recursiva = termina_recursiva - empieza_recursiva

print(f"Suma con bucle: {resultado_bucle} - Tiempo: {tiempo_bucle:.6f} segundos")
print(f"Suma con sum(): {resultado_sum} - Tiempo: {tiempo_sum:.6f} segundos")
print(f"Suma con recursividad: {resultado_recursiva} - Tiempo: {tiempo_recursiva:.6f} segundos")


# Parte 3: Invertir la lista de pedidos
# Problema: Clara quiere armar los paquetes en orden inverso al que fueron pedidos (para que el último pedido salga primero).
# Objetivo: Invertir la lista de pedidos.

empieza_reversed = time.time()
resultado_reversed = invertir_orden_reversed(lista_pedidos_1000)
termina_reversed = time.time()
tiempo_reversed = termina_reversed - empieza_reversed

empieza_slicing = time.time()
resultado_slicing = invertir_orden_slicing(lista_pedidos_1000)
termina_slicing = time.time()
tiempo_slicing = termina_slicing - empieza_slicing

empieza_bucle = time.time()
resultado_bucle = invertir_con_bucle(lista_pedidos_1000)
termina_bucle = time.time()
tiempo_bucle = termina_bucle - empieza_bucle

print(f"Invertir con reversed(): primeros 5 -> {resultado_reversed[:5]} - Tiempo: {tiempo_reversed:.6f} segundos")
print(f"Invertir con slicing:    primeros 5 -> {resultado_slicing[:5]} - Tiempo: {tiempo_slicing:.6f} segundos")
print(f"Invertir con bucle:      primeros 5 -> {resultado_bucle[:5]} - Tiempo: {tiempo_bucle:.6f} segundos")
