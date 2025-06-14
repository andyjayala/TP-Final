import random

nombres = ["Juan", "Marta", "Carlos", "Lucía", "Norma", "Alejandro", "Sofía", "Federico", "Andrea", "Daniela"]
apellidos = ["Pérez", "Gómez", "Díaz", "Fernández", "Vazquez", "López", "Rodríguez", "González", "Torres", "Castro"]

productos_disponibles = ["harina", "fideos", "arvejas", "azúcar", "sal", "arroz", "aceite", "leche", "pan", "tomate"]

# Elige un cliente aleatorio y entre 1 y 5 productos distintos también aleatoreamente para generar pedidos
def generar_pedidos(n, lista_clientes):
    pedidos = []
    for _ in range(n):
        pedido = {
            "cliente": random.choice(lista_clientes),
            "productos": random.sample(productos_disponibles, random.randint(1, 5))
        }
        pedidos.append(pedido)
    return pedidos

# Elige nombres de la lista para crear nuevas listas de diferentes cantidades
def generar_clientes_combinados(n):
    clientes = []
    for _ in range(n):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        cliente = f"{nombre} {apellido}"
        clientes.append(cliente)
    return clientes


# Crear lista de clientes combinados
lista_clientes_100 = generar_clientes_combinados(100)
lista_clientes_1000 = generar_clientes_combinados(1000)
lista_clientes_10000 = generar_clientes_combinados(10000)
lista_clientes_100000 = generar_clientes_combinados(100000)

# Crear pedidos usando esas listas
lista_pedidos_100 = generar_pedidos(100, lista_clientes_100)
lista_pedidos_1000 = generar_pedidos(1000, lista_clientes_1000)
lista_pedidos_10000 = generar_pedidos(10000, lista_clientes_10000)
lista_pedidos_100000 = generar_pedidos(100000, lista_clientes_100000)

# Crear conjunto de clientes de diferentes cantidades
conjunto_clientes_1000 = set(lista_clientes_1000)
conjunto_clientes_10000 = set(lista_clientes_10000)
conjunto_clientes_100000 = set(lista_clientes_100000)

# Crear lista de productos
lista_cantidad_productos_100 = [len(pedido["productos"]) for pedido in lista_pedidos_100]
lista_cantidad_productos_1000 = [len(pedido["productos"]) for pedido in lista_pedidos_1000]
lista_cantidad_productos_10000 = [len(pedido["productos"]) for pedido in lista_pedidos_10000]
lista_cantidad_productos_100000 = [len(pedido["productos"]) for pedido in lista_pedidos_100000]