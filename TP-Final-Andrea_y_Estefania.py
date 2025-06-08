import time
from datos import lista_pedidos_1000
from funciones import invertir_con_bucle, invertir_orden_reversed, invertir_orden_slicing

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
