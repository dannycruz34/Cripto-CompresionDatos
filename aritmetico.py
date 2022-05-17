import nltk
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
import math

cadena = "abracadabraabracadabra"
letras = nltk.Text(nltk.regexp_tokenize(cadena ,"[a-z]"))
letras = list(letras)

fdist = FreqDist(letras)   
vocabulario=fdist.keys()  
frecuencia=fdist.values() 
probabilidad = []
for i in range(0,len(vocabulario)):
    probabilidad.append(frecuencia[i]/float(len(letras)))

print probabilidad
print vocabulario

#//////////////////////////////////////////////////////////////

def codificaAritmetico( cadena ):
    low = 0.0
    high = 1.0
    rango = high - low
    for j in range(0,len(cadena)):
        intervalos = []
        intervalos.append(low)
        for i in range(0,len(vocabulario)):
            intervalos.append(rango * probabilidad[i])
            if( i > 0):
                intervalos[i] = intervalos[i] + intervalos[i-1]
        intervalos[len(vocabulario)] = intervalos[len(vocabulario)] + intervalos[len(vocabulario)-1]        
        indiceInter = vocabulario.index(cadena[j]) + 1
        print "Intervalos: " , intervalos
        print "Recalcular intervalo:",indiceInter, "   ", intervalos[indiceInter]
        high = intervalos[indiceInter]
        low = intervalos[indiceInter-1]
        rango = high - float(low)
    return high
#//////////////////////////////////////////////////////////////

def decodificador( numero , iteraciones ):
    low = 0.0
    high = 1.0
    rango = high - low
    palabra=""
    for i in range(0,iteraciones):
        intervalos = []
        intervalos.append(low)
        for i in range(0,len(vocabulario)):
            intervalos.append(rango * probabilidad[i])
            if( i > 0):
                intervalos[i] = intervalos[i] + intervalos[i-1]
        intervalos[len(vocabulario)] = intervalos[len(vocabulario)] + intervalos[len(vocabulario)-1]        
        for i in range(0,len(intervalos)-1):
            if( numero > intervalos[i] and numero <= intervalos[i+1]):
                #if len(palabra) <= len(cadena)-1:
                palabra=palabra + vocabulario[i]
                high = intervalos[i+1]
                low = intervalos[i]
                rango = high - low
        print intervalos
        print palabra
    print palabra


#//////////////////////////////////////////////////////////////

def deciBinario( numero ):
    cadena = ""
    bandera = 1
    
    while( bandera==1):
        numero = float(numero) * 2.0
        if( numero > 1.0):
            cadena = cadena + "1"
            numero = numero - 1.0
        elif (numero==1.0):
            cadena = cadena +"1"
            bandera=0
        else:
            cadena = cadena + "0"
    return cadena    
        

#//////////////////////////////////////////////////////////////

def float_to_bin(x):
  if x == 0:
    return "0" * 64
  w, sign = (float.hex(x), 0) if x > 0 else (float.hex(x)[1:], 1)
  mantissa, exp = int(w[4:17], 16), int(w[18:])
  return "{}{:011b}{:052b}".format(sign, exp + 1023, mantissa)
  
codigo = codificaAritmetico(cadena)
print codigo
decodificador(codigo,len(cadena))


bina = deciBinario(codigo)
print "Bits necesarios para la cadena original: ", 8*len(cadena)
print bina
print "Bits necesarios para el flotante: ", len(bina)
print "Factor de compresion ", len(bina), "/", len(cadena)*8, "   =   ", len(bina)/float(len(cadena)*8)

deciBinario(codigo)

print("0.64")
    
x=deciBinario(0.65)
print x
print len(x)  