import nltk
from nltk import FreqDist

#guarda el texto en un arreglo por palabra
documento = nltk.Text(nltk.regexp_tokenize(open("/Users/DanniC/Documents/INAOE_2Cuatri/Criptografia/alice_in_wonderland.txt","r").read().lower(),"[A-z' .,\n]"))
#Se crea la lista de codigos 
listaCodigo =[]
listaCodigo.append([" ",101])
listaCodigo.append(["e",11000])
listaCodigo.append(["t",11011])
listaCodigo.append(["a",11110])
listaCodigo.append(["o",11111])
listaCodigo.append(["i",10011])
listaCodigo.append(["h",10010])
listaCodigo.append(["n",10001])
listaCodigo.append(["s",110010])
listaCodigo.append(["r",110100])
listaCodigo.append(["d",111001])
listaCodigo.append(["l",111010])
listaCodigo.append(["u",1100110])
listaCodigo.append(["w",1101010])
listaCodigo.append(["g",1110000])
listaCodigo.append([",",1110001])
listaCodigo.append(["c",1110110])
listaCodigo.append(["y",1110111])
listaCodigo.append(["m",1000000])
listaCodigo.append(["f",1000010])
listaCodigo.append(["'",1000011])
listaCodigo.append(["p",11001110])
listaCodigo.append(["b",11001111])
listaCodigo.append(["k",11010111])
listaCodigo.append(["`",10000010])
listaCodigo.append([".",10000011])
listaCodigo.append(["v",110101100])
listaCodigo.append(["q",11010110100])
listaCodigo.append(["x",11010110101])
listaCodigo.append(["j",11010110110])
listaCodigo.append(["z",110101101110])
listaCodigo.append(["_",1101011011110])
listaCodigo.append(["[",11010110111110])
listaCodigo.append(["]",11010110111111])

car = [row[0] for row in listaCodigo]
cod = [row[1] for row in listaCodigo]


f = open("/Users/DanniC/Documents/INAOE_2Cuatri/Criptografia/compHuffman.txt","w") 
cadena=""
cont = 0
for caracter in documento:
    
    if caracter == "\n":
        while(len(cadena) > 7):
            sub = cadena[0:8]
            cadena=cadena[8:len(cadena)]
            n = int(sub, 2)
            f.write(chr(n))
        if(len(cadena) > 0):
            n = int(cadena, 2)
            f.write(chr(n))
        cadena = ""
        f.write("\n")
    if car.count(caracter) > 0:
        indice = car.index(caracter)
        cadena= cadena + str(cod[indice])
f.close()

        