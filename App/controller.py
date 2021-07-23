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
    loadUserTrack(catalog)
    loadContextContent(catalog)
    loadSentimentValues(catalog)

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
    return model.filtrarRequerimiento1(catalog, cat1, minCat1, maxCat1, cat2, minCat2, maxCat2)

def filtrarRequerimiento2(catalog, minLiv, maxLiv, minSpe, maxSpe):
    return model.filtrarRequerimiento2(catalog, minLiv, maxLiv, minSpe, maxSpe)

def filtrarRequerimiento3(catalog, minVal, maxVal, minTemp, maxTemp):
    return model.filtrarRequerimiento3(catalog, minVal, maxVal, minTemp, maxTemp)

def filtrarRequerimiento4(catalog, generos, pregunta, nuevoGenero, minValor, maxValor):
    return model.filtrarRequerimiento4(catalog, generos, pregunta, nuevoGenero, minValor, maxValor)

# Funciones de consulta sobre el catálogo

def buscarCaracteristica(catalog, caracteristica):
    return model.buscarCaracteristica(catalog, caracteristica)

