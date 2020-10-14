# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:51:54 2020

@author: Jorge
"""

import serial
import time

puerto = "COM3" 
baudio = 9600
i = 0

esp32 = serial.Serial(puerto, baudio) #Defino el objeto ESP señalando el puerto al que tiene que mirar y la frecuencia de muestreo
time.sleep(2)                         #Espero 2s para que se acople el puerto serie
esp32.close()                         #Cierro el puerto para reiniciar el dispositivo

def leeLinea():
    if(esp32.isOpen() == False):
        esp32.open()
    salida = esp32.readline()
    return salida

while i < 20:
    valor = leeLinea()    
    print(valor(2,-5))
    i = i + 1
    #`print(i)
type(valor)
esp32.close()
