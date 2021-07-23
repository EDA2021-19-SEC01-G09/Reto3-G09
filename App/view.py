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
from DISClib.ADT import map as mp
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

def imprimirReq4(respuesta, generos):
    for i in generos:
        print('=========== ' + str(i) + ' ===========')
        print('El total de eventos de escucha de este genero son: ' + str((mp.get(respuesta[1], i))['value'][1]))
        print('El total de artistas únicos es de: ' + str((mp.get(respuesta[1], i))['value'][0]))
        print('Algunos artistas para ' + str(i))
        for artistas in ((mp.get(respuesta[1], i))['value'][2])['elements']:
            print(artistas)

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
        tupla = controller.loadData(catalog)
        print('Se cargaron: ' + str(lt.size(catalog['todos'])))
        print('Se cargaron: ' + str(lt.size(catalog['artistas'])) + ' artistas diferentes')
        print('Se cargaron: ' + str(lt.size(catalog['identificadores'])) + ' eventos diferentes')
        print('A continuación se presentan los 5 primeros y 5 últimos eventos de escucha registrados: ')
        displayCarga(catalog['todos'])
        print("Tiempo [ms]: ", f"{tupla[0]:.3f}", "  ||  ",
                            "Memoria [kB]: ", f"{tupla[1]:.3f}")
        

    elif int(inputs[0]) == 3:
        cat1 = input('Ingrese el nombre de la característica 1: ')

        if controller.buscarCaracteristica(catalog, cat1) == True:
            minCat1 = (input('Ingrese el valor mínimo de la característica 1: '))
            maxCat1 = (input('Ingrese el valor máximo de la característica 1: '))
            cat2 = input('Ingrese el nombre de la característica 2: ')

            if controller.buscarCaracteristica(catalog, cat2) == True:
                minCat2 = (input('Ingrese el valor mínimo de la característica 2: '))
                maxCat2 = (input('Ingrese el valor máximo de la característica 2: '))
                tupla = controller.filtrarRequerimiento1(catalog, cat1, minCat1, maxCat1, cat2, minCat2, maxCat2)
                respuesta = tupla[0]
                print('----------------------------------------------------------------')
                print('El total de eventos de escucha registrados son: ' + str(respuesta[0]))
                print('El número de artistas (sin repetición) registrados son: ' + str(respuesta[1]))
                print("Tiempo [ms]: ", f"{tupla[1]:.3f}", "  ||  ",
                            "Memoria [kB]: ", f"{tupla[2]:.3f}")


            else:
                print('La característica ingresada no existe')

        else:
            print('La característica ingresada no existe')

    elif int(inputs[0]) == 4:
        minLiv = input('Ingrese el valor mínimo de liveness: ')
        maxLiv = input('Ingrese el valor máximo de liveness: ')
        minSpe = input('Ingrese el valor mínimo de speechiness: ')
        maxSpe = input('Ingrese el valor máximo de speechiness: ')
        tupla = controller.filtrarRequerimiento2(catalog, minLiv, maxLiv, minSpe, maxSpe)
        respuesta = tupla[0]
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

        print("Tiempo [ms]: ", f"{tupla[1]:.3f}", "  ||  ",
                            "Memoria [kB]: ", f"{tupla[2]:.3f}")


    elif int(inputs[0]) == 5:
        minVal = input('Ingrese el valor mínimo de valence: ')
        maxVal = input('Ingrese el valor máximo de valence: ')
        minTemp = input('Ingrese el valor mínimo de tempo: ')
        maxTemp = input('Ingrese el valor máximo de tempo: ')
        tupla = controller.filtrarRequerimiento3(catalog, minVal, maxVal, minTemp, maxTemp)
        respuesta = tupla[0]
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

        print("Tiempo [ms]: ", f"{tupla[1]:.3f}", "  ||  ",
                            "Memoria [kB]: ", f"{tupla[2]:.3f}")


    elif int(inputs[0]) == 6:
        print('Genero         BPM Típico')
        print('Reggae          60 a 90')
        print('Down-tempo      70 a 100')
        print('Chill-out       90 a 120')
        print('Hip-hop         85 a 115')
        print('Jazz and Funk  120 a 125')
        print('Pop            100 a 130')
        print('R&B             60 a 80')
        print('Rock           110 a 140')
        print('Metal          100 a 160')

        pregunta = int(input('Si desea ingresar un nuevo genero pulse "1" de lo contrario pulse "0": '))
        if pregunta == 1:
            nuevoGenero = input('Ingrese el nombre del genero: ')
            minValor = (input('Ingrese el valor minimo del rango de Tempo del genero: '))
            maxValor = (input('Ingrese el valor maximo del rango de Tempo del genero: '))
        else:
            nuevoGenero = None
            minValor = None
            maxValor = None

        lista = input('Ingrese la lista de generos que desea buscar (separados por "," y sin espacios): ')
        generos = lista.lower().strip().split(",")
        tupla = controller.filtrarRequerimiento4(catalog, generos, pregunta, nuevoGenero, minValor, maxValor)
        respuesta = tupla[0]
        print('------------------------------------------------------------------')
        print('El total de eventos de escucha o reproducciones es de: ' + str(respuesta[0]))
        imprimirReq4(respuesta, generos)
        print("Tiempo [ms]: ", f"{tupla[1]:.3f}", "  ||  ",
                            "Memoria [kB]: ", f"{tupla[2]:.3f}")


    else:
        sys.exit(0)
sys.exit(0)
