"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import time
import tracemalloc
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(catalog):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadUserTrack(catalog)
    loadContextContent(catalog)
    loadSentimentValues(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory

def loadUserTrack(catalog):
    archivo = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(archivo, encoding='utf-8'), delimiter = ",")
    
    for file in input_file:
        model.addHashtag(catalog, file)

def loadContextContent(catalog):
    archivo = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(archivo, encoding='utf-8'), delimiter = ",")
    
    for file in input_file:
        model.addEvento(catalog, file)

def loadSentimentValues(catalog):
    archivo = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(archivo, encoding='utf-8'), delimiter = ",")
    
    for file in input_file:
        model.addSentimiento(catalog, file['hashtag'], file)

# Funciones de ordenamiento

def filtrarRequerimiento1(catalog, cat1, minCat1, maxCat1, cat2, minCat2, maxCat2):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    answer = model.filtrarRequerimiento1(catalog, cat1, minCat1, maxCat1, cat2, minCat2, maxCat2)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory


def filtrarRequerimiento2(catalog, minLiv, maxLiv, minSpe, maxSpe):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    answer = model.filtrarRequerimiento2(catalog, minLiv, maxLiv, minSpe, maxSpe)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory

def filtrarRequerimiento3(catalog, minVal, maxVal, minTemp, maxTemp):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    answer = model.filtrarRequerimiento3(catalog, minVal, maxVal, minTemp, maxTemp)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory


def filtrarRequerimiento4(catalog, generos, pregunta, nuevoGenero, minValor, maxValor):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    answer = model.filtrarRequerimiento4(catalog, generos, pregunta, nuevoGenero, minValor, maxValor)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory

# Funciones de consulta sobre el catálogo

def buscarCaracteristica(catalog, caracteristica):
    return model.buscarCaracteristica(catalog, caracteristica)

# ======================================
# Funciones para medir tiempo y memoria
# ======================================


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
