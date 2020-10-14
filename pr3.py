# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:51:54 2020

@author: Jorge
"""

import serial
import time
import pandas as pd
import matplotlib.pyplot as plt

puerto = "COM3" 
baudio = 115200
i = 0
segundos = 5

esp32 = serial.Serial(puerto, baudio) #Defino el objeto ESP señalando el puerto al que tiene que mirar y la frecuencia de muestreo
time.sleep(2)                         #Espero 2s para que se acople el puerto serie
esp32.close()                         #Cierro el puerto para reiniciar el dispositivo

listaTitulos = ["Tiempo", "Aceleración en X", "Aceleración en Y", "Aceleración en Z", "Giroscopo en X", "Giroscopo en Y", "Giroscopo en Z"]

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

def calculoDatos(nombreFichero):
    df = pd.read_csv(nombreFichero, ";")
    print("He leido el fichero")
    #filas, columnas = df.shape
    #print(df.columns)
    med = df.mean()   #Devuelve una lista con la media de cada columna
    var = df.var()    #Devuelve una lista con la varianza de cada columna
    return med, var

def dibujoGraficaArchivo(nombreFichero):
    df = pd.read_csv(nombreFichero, ";")
    ejeX = df.iloc[:,0]     #Valores de la primera columna de pandas
    (filas, columnas_size) = df.shape
    for index, columnas in enumerate(df.columns):
        plt.figure()
        plt.title(listaTitulos[index])      #El título del grafico
        ejeY = df.iloc[:,index]
        #plt.subplot(2, round((columnas_size/2) + 0.5) , index) #Nº de filas, nº de columnas, indice de la figura
        plt.plot(ejeX, ejeY)
        plt.show()
    print("He pintado  las graficas")

escribeFichero("datos.txt", "", "w")    
escribeFichero("auxiliar.txt", "", "w")
t_ref = time.time()

while i < 11:
    valor = leeLinea()   
    if i > 8:
        t_anterior = time.time()
        t_actual = time.time()
        while ((t_actual - t_anterior) < segundos):
            t_actual = time.time()
            escribeFichero("datos.txt", str(t_actual - t_ref), "a")
            escribeFichero("datos.txt", ";", "a")
            linea = leeLinea()
            escribeFichero("datos.txt", linea, "ab")
            escribeFichero("auxiliar.txt", linea, "ab")
        dibujoGraficaArchivo("datos.txt")
        media5s, varianza5s = calculoDatos("auxiliar.txt")
        #print("Media:", "\n" , media5s)
        #print("Varianza:", "\n" , varianza5s)
        escribeFichero("auxiliar.txt","", "w") #con esta linea borro todos los datos de aux
    i = i + 1
    
esp32.close()
