# Triangulo de pascal

def factorial(number):
    if(number == 0):
        return 1
    else:

        aux = 1
        #number(number-1)(number-2)
        for x in range(number):
            aux *= (x+1)
        
        
        return aux


def coefBinomial(n,p):
    var = factorial(n)
    vardois = factorial(p) * factorial(n-p)
    return var / vardois

def trianguloDePascal(linha):
    
    #linha,coluna
    
    for x in range(linha):
        matriz = []
        for y in range(x):
            matriz.append(int(coefBinomial(x,y)))       
        matriz.append(1)
        print("P(" , x , ") = ",*matriz)


trianguloDePascal(15)
