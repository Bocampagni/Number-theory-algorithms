##Se p é primo, então b ^ (p - 1) é congruente modulo p.


p = int(input("Entre um número primo: "))
b = int(input("Entre uma base: "))


fermat = b ** (p - 1)
print(fermat, "é congruente a 1 módulo", p)


##A ordem de b é o menor inteiro i que faz com que b^i seja congruente modulo p.
##A ordem de b divide p - 1.

possiveisOrdens = []
for c in range(1, p):
    if (p - 1) % c == 0:
        possiveisOrdens.append(c)


print("Posssiveis ordens: ", possiveisOrdens)


## A ordem de b precisa ser congruente modulo p.
for c in possiveisOrdens:
    if((b**c) % p == 1):
        print("A ordem é: ", c)
        break


