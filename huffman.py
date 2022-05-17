
import nltk
from nltk import FreqDist

doc = nltk.Text(nltk.regexp_tokenize(open("/Users/DanniC/Documents/INAOE_2Cuatri/Criptografia/alice_in_wonderland.txt","r").read().lower(),"[A-z' .,]"))
fdist = FreqDist(doc)   
vocabulario=fdist.keys()  
frecuencia=fdist.values()  

print vocabulario
prob = []
proba = 0
cont = 0
for fr in frecuencia:
    lol =  fr/float(len(doc))
    prob.append(lol)
    print lol
    proba = proba + lol
    cont = cont + 1

print proba
print  "Longitud de Alfabeto: " + str(len(vocabulario))
print len(doc)
print "Frecuencia: "
print frecuencia

listaLetras = []
for i in range(0,len(vocabulario)):
	for j in range(i,len(vocabulario)):
		if prob[j] < prob[i]:
			aux = prob[j]
			prob[j] = prob[i]
			prob[i] = aux

			aux2 = vocabulario[j]
			vocabulario[j] = vocabulario[i]
			vocabulario[i] = aux2
#CAMBIAR AQUI LAS FRECUENCIAS
	listaLetras.append([vocabulario[i],prob[i],frecuencia[i]])


def ordenarMenorMayor(listaLetras):
	for i in range(0,len(listaLetras)):
		for j in range(i,len(listaLetras)):
			x = listaLetras[j]
			y = listaLetras[i]
			if x[1] < y[1]:
				aux = listaLetras[j]
				listaLetras[j] = listaLetras[i]
				listaLetras[i] = aux
				pass
	pass
	return listaLetras

for i in range(0,len(vocabulario)):
	print str(i) + "\t" + str(vocabulario[i]) + "   " + str(prob[i]) + "   " + str(frecuencia[i])

#print "Lista creada: " 
#print listaLetras

nodos = dict()

while len(listaLetras) > 1:
	# tomamos los dos nodos menores a unir...
	der = listaLetras[0]
	izq = listaLetras[1]
	if len(listaLetras):
	    print " Concatenacion: " + izq[0] + " + " + der[0]
	    print " Suma: " + str(izq[1]) + " + " + str(der[1]) + " = " + str(izq[1] + der[1])
	# los unimos...def buscarCodigoLetra(nodoActual, nodos, nodoFinal):
	valorNodo = izq[1] + der[1]
	nodos[izq[0], valorNodo] = 0
	nodos[der[0], valorNodo] = 1
	# creeamos el nuevo nodo...
	listaLetras.append([izq[0] + "" + der[0], valorNodo])
	# eliminamos los nodos procesados...
	listaLetras.pop(0)
	listaLetras.pop(0)
	# ordenamos de menor a mayor
	listaLetras = ordenarMenorMayor(listaLetras)
#	print "Lista ordenada: " 
#	print listaLetras
nodos = nodos.items()
for nodo in nodos:
    print nodo



