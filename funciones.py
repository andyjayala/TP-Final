import time
import tracemalloc

# Parte 1: Diferenciar entre buscar en una lista y un conjunto
def buscar_en_lista(nombre, lista_clientes):
    return nombre in lista_clientes

def buscar_en_conjunto(nombre, conjunto_clientes):
    return nombre in conjunto_clientes

# Parte 2: Diferenciar entre sumar con bucle, sum o recursividad
def suma_bucle(lista):
    suma = 0
    for cantidad in lista:
        suma += cantidad
    return suma

def suma_con_sum(lista):
    return sum(lista)

def suma_con_recursividad(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_con_recursividad(lista[1:])

# Parte 3: Diferenciar entre invertir orden con reversed, slicing o bucle
def invertir_orden_reversed(lista):
    return list(reversed(lista))

def invertir_orden_slicing(lista):
    return lista[::-1]

def invertir_con_bucle(lista):
    nueva_lista = []
    for i in range(len(lista)-1, -1, -1):
        nueva_lista.append(lista[i])
    return nueva_lista

# Función para medir tiempo y memoria de la ejecución de cada función generada anteriormente
def medir_tiempo_y_memoria(func, *args):
    tracemalloc.start()
    tiempo_de_inicio = time.time()
    resultado_de_la_funcion = func(*args)
    tiempo_de_finalización = time.time() 
    tiempo_transcurrido = tiempo_de_finalización - tiempo_de_inicio
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return resultado_de_la_funcion, tiempo_transcurrido, memoria_actual, memoria_maxima