# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:17:01 2026

@author: justo
"""

def registrar_habitos():
    lista_act = []
    while True:
        actividad = input("Ingrese actividad realizada ")
        lista_act.append(actividad)
        if actividad == "Termine":
            break
    return lista_act

"""
La funcion registrar habitos va a solicitarle al usuario que ingrese sus actividades, \
con ellas va a realizar una lista donde especifique dichas actividades. La funcion se va a ver interrumpida\
cuando el ususario especifique que termino.

Parámetros
----------
No hay parametro, se llama a la funcion para obtener ejecutar el input

Returns
-------
lista
la devolucion de esta funcion va a ser la lista con las actividades que realiza usualmente
"""    
    
def analizar_habitos(lista): 
    diccionario_actividades = {}
    for i in lista:
        if i not in diccionario_actividades:
            diccionario_actividades [i] = 1 
        if i in diccionario_actividades:
            diccionario_actividades [i] += 1 
     
    return diccionario_actividades       
            
"""
La funcion analizar habitos va a recibir una lista de activiadades.\
luego va a recorrer la lista y determinar la frecuencia de realizacion de estas actividades.

Parámetros
----------
lista = lista
Se recibe una lista resultante de otra funcion donde se determinan las actividades del usuario

Returns
-------
diccionario
la devolucion de esta funcion va a ser un diccionario con las actividades y la cantidad de veces que se realizo
"""  
    