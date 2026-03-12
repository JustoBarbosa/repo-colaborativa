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
    
    
def analizar_habitos(lista): 
    diccionario_actividades = {}
    for i in lista:
        if i not in diccionario_actividades:
            diccionario_actividades [i] = 1 
        if i in diccionario_actividades:
            diccionario_actividades [i] += 1 
     
    return diccionario_actividades       
            
           
    
    