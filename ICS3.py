from math import gcd

def RSA(p: int, q: int, message: int):
    n = p*q

    t = (p-1)*(q-1)

    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

    ct = (message ** e) % n
    print(f"Encrypted message is {ct}")

    mes = (ct ** d) % n
    print(f"Decrypted  message is {mes}")

RSA(p=23, q=59, message=94)

RSA(p=3, q=7, message=12)