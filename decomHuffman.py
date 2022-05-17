###Descompresor


fr = open("/Users/DanniC/Documents/INAOE_2Cuatri/Criptografia/compHuffman.txt","r")
f = open("/Users/DanniC/Documents/INAOE_2Cuatri/Criptografia/AliceDescomprimir.txt","w") 

def decodificar( linea , f ):
    print linea
    vectorCodigo = [str(row[1]) for row in listaCodigo]
    encontrado=0
    tam = 14
    while len(linea) > 13:
        if encontrado==1:
            if len(linea) >13 : 
                tam = 14
                encontrado=0
            else:
                tam=len(linea)
                encontrado=0
        codigo  = linea[0:tam]
        exist = vectorCodigo.count(codigo)
        if exist > 0:
            indice = vectorCodigo.index(codigo)
            letra = listaCodigo[indice][0]
            linea = linea[len(codigo):len(linea)]
            f.write(letra)
            print codigo
            print letra
            encontrado=1
        else:
            tam=tam-1
            
    f.write("\n")




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

documento = []
for line in fr:
    for i in range(0,len(line)):
        documento.append(line[i])

codigo = ""
for caracter in documento:
    if caracter == '\n':
        decodificar( codigo, f )
        codigo = ""
    else:    
        bina = "00000000"
        entero = ord(caracter)
        binario = bin(entero)
        binario = binario[2:len(binario)]
        n= len(binario)
        binario = bina + binario
        binario = binario[n:len(binario)] 
        codigo = codigo + binario
f.close()




