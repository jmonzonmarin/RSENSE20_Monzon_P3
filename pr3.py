# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:51:54 2020

@author: Jorge
"""

import serial
import time

puerto = "COM3" 
baudio = 115200
i = 0

esp32 = serial.Serial(puerto, baudio) #Defino el objeto ESP señalando el puerto al que tiene que mirar y la frecuencia de muestreo
time.sleep(2)                         #Espero 2s para que se acople el puerto serie
esp32.close()                         #Cierro el puerto para reiniciar el dispositivo

def leeLinea():
    if(esp32.isOpen() == False):
        esp32.open()
    salida = esp32.readline()
    #salida = esp32.read()
    return salida

def escribeFichero(nombre, dato, tipo):
    f = open(nombre, tipo)
    f.write(dato)        # '\n' añade un salto de linea a la frase
    #f.write('\n')
    f.close()

escribeFichero("datos.txt", "", "w")    

while i < 20:
    valor = leeLinea()   
    if i > 8:
        escribeFichero("datos.txt", valor, "ab")    #ab indica que estamos concatenando valores de bytes
        print(valor)
    i = i + 1
    
type(valor)
esp32.close()
