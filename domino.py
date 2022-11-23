while True:
    try:
        n = int(input())
        if 0 <= n <= 10000:
             print(int(((n + 1)*(n + 2))/2))
        break
    except ValueError:
        print("n deve estar entre 0 e 10.000! \n Tente  novamente!")

