# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:51:54 2020

@author: Jorge
"""

import serial
import time

puerto = "COM3" 
baudio = 9600

ESP = serial.Serial(puerto, baudio) #Defino el objeto ESP señalando el puerto al que tiene que mirar y la frecuencia de muestreo
time.sleep(2)                        #Espero 2s para que se acople el puerto serie

def leeLinea():
    ESP.open()
    salida = ESP.readline()
    ESP.close()
    return salida

valor = leeLinea()

print(valor)