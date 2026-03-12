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
    
     