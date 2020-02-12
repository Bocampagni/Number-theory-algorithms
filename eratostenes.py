def primeNumber( n):
    p=int(n** 0.5)
    while p >=1:
        if n%p ==0 and p !=1:
            break
        if p ==1:
            return True
        p=p -1



primos =[]    
n=int( input ("Até onde quer ir ?"))
for i in range (2 , n +1) :
    if primeNumber (i) :
        primos.append ( i)
print ("Primos até %d são " %n , primos )