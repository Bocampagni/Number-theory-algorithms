import math

def fermat(inteiro, num):
    inteiro+= 1  ##Soma-se porque o quadrado da parte inteira não corresponde ao número inicial

    lista = []
    y = 0
    x = 0
    resultado = 1


    ##Se x^2 - y^2 - num = 0, então achamos os fatores de num primos.
    while resultado != 0:
        x = int(math.pow(inteiro,2))
        y = int(math.sqrt(x - num))
        resultado = int(x - math.pow(y,2) - num)
        inteiro += 1

    ##-1 por causa do inteiro  +=1 da última iteração do while.
    lista.append(inteiro - 1 + y);
    lista.append(inteiro - 1 - y);

    return lista
    



print("Método de fatoração de Fermat: ")

num = float(input("Entre um número composto: "))

inteiro = int(math.sqrt(num))

if(math.pow(inteiro, 2) == num):
    print(inteiro)
else:
    fatores = fermat(inteiro, num)
    print("Os fatores de  ", num, " são: ", fatores)



