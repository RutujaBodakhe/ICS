def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def main():
    p = 23
    print("The value of p : ", p)

    G = 9
    print("The value of G : ", G)

    a = 4
    print("The private key a for Alice : ", a)

    x = power(G, a, p)
    b = 3
    print("The private key b for Bob : ", b)

    y = power(G, b, p)

    ka = power(y, a, p)
    kb = power(x, b, p)

    print("Secret key for Alice is : ", ka)
    print("Secret key for Bob is : ", kb)

if __name__ == "__main__":
    main()
