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

