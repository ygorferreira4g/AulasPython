for numero in range(1, 101):
    c = 0
    for i in range(2, numero):
        if numero%i==0:
            c += 1
            break
    if c == 0:
        print(numero, "primo")