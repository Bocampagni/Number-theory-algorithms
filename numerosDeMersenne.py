def primo(n):
    p = int(n ** 0.5)
    while p >= 1:
        if n%p == 0 and p !=1:
            return False

        if p == 1:
            return True
        p = p - 1

primosDeMersenne = []

n = int(input("n: "))
for c in range(2, n + 1):
    if primo(c):
        primosDeMersenne.append(c)

mersenne = []
for c in primosDeMersenne:
        if primo (2**c -1):
            mersenne.append ("2^%d - 1"%c)
print (mersenne)