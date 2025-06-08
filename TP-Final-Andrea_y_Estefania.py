# Parte 1: Buscar si un cliente hizo un pedido
# Problema: Tiene una lista de nombres de clientes que hicieron pedidos hoy.
# Objetivo: Saber si Juan Pérez está en la lista.
# Comparación: Buscar en una lista vs. un conjunto.
# Resultado: El conjunto es mucho más rápido si hay muchos pedidos.
# Analogía: Revisar uno por uno (lista) vs tener los nombres ya clasificados en una caja con separadores (set).

import time

# lista_cliente = ["Juan", "Andrea", "Tefi", "Fulanito", "Miriam", "Agustin", "Scaloni", "Pamela"]

# start_listas = time.time()

# for cliente in lista_cliente:
#     if cliente == "Juan":
#         print("Juan está en la lista")
#     else:
#         print("Juan no está")

# end_listas = time.time()

# print(f"Código con listas: {end_listas-start_listas:.6f}")

# print("Juan está en la lista") if "Juan" in lista_cliente else print("Juan no está en la lista")

# esta_en_la_lista = "Juan" in lista_cliente

# if esta_en_la_lista == True: # = if esta_en_la_lista
#     print("Juan está")
# else:
#     print("No está")

# print("Juan está en la lista") if esta_en_la_lista else print("Juan no está en la lista")


# conjunto_clientes = {"Juan", "Andrea", "Tefi", "Fulanito", "Miriam", "Agustin", "Scaloni", "Pamela"}
# start_set = time.time()
# print("Juan está") if "Juan" in conjunto_clientes else print("Juan no está")

# end_set = time.time()

# print(f"Código con set: {end_set-start_set:.6f}")

# probando_set = set(lista_cliente)

# print("Juan está") if "Juan" in conjunto_clientes else print("Juan no está")

# print("Juan en lista") if "Juan" in probando_set else print("no está")


# Parte 3: Invertir la lista de pedidos
# Problema: Clara quiere armar los paquetes en orden inverso al que fueron pedidos (para que el último pedido salga primero).
# Objetivo: Invertir la lista de pedidos.
# Comparación: Slicing ([::-1]) vs reversed() vs bucle manual.
# Resultado: [::-1] es el más rápido.
# Analogía: Dar vuelta una pila de hojas a mano (bucle) vs tener una bandeja que ya invierte el orden automáticamente ([::-1]).

lista_pedidos = ["harina", "arroz", "fideos", "azucar", "sal", "arvejas","harina", "arroz", "fideos", "azucar", "sal", "arvejas"]*1000

# start_reversed= time.time()
def invertir_orden_reversed(lista_pedidos):
    nueva_lista = list(reversed(lista_pedidos))
    return nueva_lista
# end_reversed = time.time()

# start_slicing= time.time()
def invertir_orden_slicing(lista_pedidos):
    return lista_pedidos[::-1]
# end_slicing = time.time()

# start_bucle= time.time()
nueva_lista=[]
def invertir_con_bucle(lista_pedidos):
    for i in range (len(lista_pedidos)-1, -1, -1):
        nueva_lista.append(lista_pedidos[i])
    return nueva_lista
# end_bucle = time.time()

start_reversed= time.time()
invertir_orden_reversed(lista_pedidos)
end_reversed = time.time()

start_slicing= time.time()
invertir_orden_slicing(lista_pedidos)
end_slicing = time.time()

start_bucle= time.time()
invertir_con_bucle(lista_pedidos)
end_bucle = time.time()

print(f"Código con reversed: {end_reversed-start_reversed:.20f}, código con slicing: {end_slicing-start_slicing:.20f} y código con bucle: {end_bucle-start_bucle:.20f}")