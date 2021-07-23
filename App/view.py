"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf
import sys
import random


default_limit = 1000
sys.setrecursionlimit(default_limit*100)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de crimenes")
    print("3- Caracterizar las reproducciones")
    print("4- Encontrar música para festejar")
    print("5- Encontrar música para estudiar")
    print("6- Estudiar los géneros musicales")
    print("0- Salir")
    print("*******************************************")


def displayCarga(lst):
    final = lt.size(lst) + 1
    posiciones = list(range(1, 6)) + list(range(final - 5, final))
    for pos in posiciones:
        event = lt.getElement(lst, pos)
        print(event)

def displayRandom(lst, car1, car2, n = 8):
    txt = list(range(1, n + 1))
    selecc = random.sample(list(range(1, lt.size(lst) + 1)), n)
    for x, y in zip(txt, selecc):
        event = lt.getElement(lst, y)
        print('Track ' + str(x) + ': ' + str(event['track_id']) + ' con ' + car1 + " " + str(event[car1]) + " y " + car2 + " " + str(event[car2]))


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # catalog es el controlador que se usará de acá en adelante
        catalog = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de eventos musicales....")
        controller.loadData(catalog)
        print('Se cargaron: ' + str(lt.size(catalog['todos'])))
        print('Se cargaron: ' + str(lt.size(catalog['artistas'])) + ' artistas diferentes')
        print('Se cargaron: ' + str(lt.size(catalog['identificadores'])) + ' eventos diferentes')
        print('A continuación se presentan los 5 primeros y 5 últimos eventos de escucha registrados: ')
        displayCarga(catalog['todos'])
        

    elif int(inputs[0]) == 3:
        cat1 = input('Ingrese el nombre de la característica 1: ')

        if controller.buscarCaracteristica(catalog, cat1) == True:
            minCat1 = (input('Ingrese el valor mínimo de la característica 1: '))
            maxCat1 = (input('Ingrese el valor máximo de la característica 1: '))
            cat2 = input('Ingrese el nombre de la característica 2: ')

            if controller.buscarCaracteristica(catalog, cat2) == True:
                minCat2 = (input('Ingrese el valor mínimo de la característica 2: '))
                maxCat2 = (input('Ingrese el valor máximo de la característica 2: '))
                respuesta = controller.filtrarRequerimiento1(catalog, cat1, minCat1, maxCat1, cat2, minCat2, maxCat2)
                print('----------------------------------------------------------------')
                print('El total de eventos de escucha registrados son: ' + str(respuesta[0]))
                print('El número de artistas (sin repetición) registrados son: ' + str(respuesta[1]))

            else:
                print('La característica ingresada no existe')

        else:
            print('La característica ingresada no existe')

    elif int(inputs[0]) == 4:
        minLiv = input('Ingrese el valor mínimo de liveness: ')
        maxLiv = input('Ingrese el valor máximo de liveness: ')
        minSpe = input('Ingrese el valor mínimo de speechiness: ')
        maxSpe = input('Ingrese el valor máximo de speechiness: ')
        respuesta = controller.filtrarRequerimiento2(catalog, minLiv, maxLiv, minSpe, maxSpe)
        print('----------------------------------------------------------------')
        print('El total de pistas únicas en los eventos de escucha es: ' + str(lt.size(respuesta[1])))
        print('----------------------------------------------------------------')
        print('\n------------------Selección aleatoria de pistas-----------------')
        
        if lt.size(respuesta[0]) < 8:
            print('-----------El filtro elegido tiene menos de 8 pistas------------')
            displayRandom(respuesta[0], "liveness", "speechiness", lt.size(respuesta[0]))
        
        else:
            print('----------------------Se presentan 8 pistas---------------------')
            displayRandom(respuesta[0], "liveness", "speechiness")

    elif int(inputs[0]) == 5:
        minVal = input('Ingrese el valor mínimo de valence: ')
        maxVal = input('Ingrese el valor máximo de valence: ')
        minTemp = input('Ingrese el valor mínimo de tempo: ')
        maxTemp = input('Ingrese el valor máximo de tempo: ')
        respuesta = controller.filtrarRequerimiento3(catalog, minVal, maxVal, minTemp, maxTemp)
        print('----------------------------------------------------------------')
        print('El total de pistas únicas en los eventos de escucha es: ' + str(lt.size(respuesta[1])))
        print('----------------------------------------------------------------')
        print('\n------------------Selección aleatoria de pistas-----------------')

        if lt.size(respuesta[0]) < 8:
            print('-----------El filtro elegido tiene menos de 8 pistas------------')
            displayRandom(respuesta[0], "valence", "tempo", lt.size(respuesta[0]))
        
        else:
            print('----------------------Se presentan 8 pistas---------------------')
            displayRandom(respuesta[0], "valence", "tempo")

    else:
        sys.exit(0)
sys.exit(0)
