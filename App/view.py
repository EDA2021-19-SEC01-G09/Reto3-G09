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
        print(catalog['sentimientos'])

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

                


    else:
        sys.exit(0)
sys.exit(0)
