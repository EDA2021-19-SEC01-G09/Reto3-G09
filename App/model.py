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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.ADT import orderedmap as om
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    catalog = { 'todos': None,
                'instrumentalness': None,
                'liveness': None,
                'speechiness': None,
                'danceability': None,
                'valence': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'energy': None,
                'hashtag': None,
                'sentimientos': None
                }
    catalog['todos'] = lt.newList('SINGLE_LINKED', compareIds)

    catalog['instrumentalness'] = om.newMap(omaptype = 'RBT',
                                      comparefunction = compare)

    catalog['liveness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['speechiness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['danceability'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['valence'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['loudness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['tempo'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['acousticness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['energy'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['hashtag'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    catalog['sentimientos']= mp.newMap(211,
                                   maptype = 'PROBING',
                                   loadfactor = 0.5,
                                   comparefunction = comparesentimientos)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addEvento(catalog, evento):
    lt.addLast(catalog['todos'], evento)
    addInstrumentalness(catalog['instrumentalness'], evento)
    addLiveness(catalog['liveness'], evento)
    addSpeechiness(catalog['speechiness'], evento)
    addDanceability(catalog['danceability'], evento)
    addValence(catalog['valence'], evento)
    addLoudness(catalog['loudness'], evento)
    addTempo(catalog['tempo'], evento)
    addAcousticness(catalog['acousticness'], evento)
    addEnergy(catalog['energy'], evento)

    return catalog

def addHashtag(catalog, evento):
    entry = om.get(catalog['hashtag'], evento['hashtag'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog['hashtag'], evento['hashtag'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addSentimiento(catalog, sentimiento, evento):
    exists = mp.contains(catalog['sentimientos'], sentimiento)
    if exists:
        entry = mp.get(catalog['sentimientos'], sentimiento)
        valor = me.getValue(entry)
    else:
        valor = newSentimiento(sentimiento)
        mp.put(catalog['sentimientos'], sentimiento, valor)
    lt.addLast(valor['sentimientos'], evento)

def newSentimiento(nuevo):
    entry = {'hashtag': "", 
             'sentimientos': None}
    entry['hashtag'] = nuevo
    entry['sentimientos'] = lt.newList('ARRAY_LIST', comparesentimientos)
    return entry

def addInstrumentalness(catalog, evento):
    entry = om.get(catalog, evento['instrumentalness'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['instrumentalness'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addLiveness(catalog, evento):
    entry = om.get(catalog, evento['liveness'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['liveness'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addSpeechiness(catalog, evento):
    entry = om.get(catalog, evento['speechiness'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['speechiness'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addDanceability(catalog, evento):
    entry = om.get(catalog, evento['danceability'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['danceability'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addValence(catalog, evento):
    entry = om.get(catalog, evento['valence'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['valence'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addLoudness(catalog, evento):
    entry = om.get(catalog, evento['loudness'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['loudness'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addTempo(catalog, evento):
    entry = om.get(catalog, evento['tempo'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['tempo'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addAcousticness(catalog, evento):
    entry = om.get(catalog, evento['acousticness'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['acousticness'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def addEnergy(catalog, evento):
    entry = om.get(catalog, evento['energy'])
    if entry is None:
        newEntry = newdata()
        om.put(catalog, evento['energy'], newEntry)
    else:
        newEntry = me.getValue(entry)
    lt.addLast(newEntry, evento)
    return catalog

def newdata():
    entry = lt.newList('SINGLE_LINKED', compare)
    return entry


# Funciones para creacion de datos

# Funciones de consulta

def filtrarRequerimiento1(catalog, cat1, minCat1, maxCat1, cat2, minCat2, maxCat2):
    lista1 = om.values(catalog[cat1], minCat1, maxCat1)
    lista2 = om.values(catalog[cat2], minCat2, maxCat2)
    listaCanciones = lt.newList('ARRAY_LIST')
    listaFinalCanciones = lt.newList('ARRAY_LIST')
    listaArtistas = lt.newList('ARRAY_LIST')
    listaFinalArtistas = lt.newList('ARRAY_LIST')

    for i in lt.iterator(lista1):
        for j in lt.iterator(i):
            lt.addLast(listaCanciones, j['track_id'])
            if lt.isPresent(listaArtistas, j['artist_id']) == 0:
                lt.addLast(listaArtistas, j['artist_id'])

    for i in lt.iterator(lista2):
        for j in lt.iterator(i):
            if lt.isPresent(listaCanciones, j['track_id']) != 0:
                lt.addLast(listaFinalCanciones, j['track_id'])
                if lt.isPresent(listaFinalArtistas, j['artist_id']) == 0:
                    lt.addLast(listaFinalArtistas, j['artist_id'])

    return lista1
            
    
def buscarCaracteristica(catalog, caracteristica):
    lista = lt.newList('ARRAY_LIST')
    for i in catalog:
        lt.addLast(lista, i)
    if lt.isPresent(lista, caracteristica) != 0:
        return True
    else:
        return False



# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):
    if (id1['track_id'] == id2['track_id']):
        return 0
    elif (id1['track_id'] > id2['track_id']):
        return 1
    else:
        return -1

def compare(eve1, eve2):
  
    if (eve1 == eve2):
        return 0
    elif (eve1 > eve2):
        return 1
    else:
        return -1

def comparesentimientos(id, entry):
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1

# Funciones de ordenamiento
