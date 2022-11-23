while True:
    try:
        a = int(input())
        m = int(input())
        if a <= 50 and m <= 50:
                if a + m <= 50:
                        print("S")
                else:
                        print("N")
        break
    except ValueError:
        print("Capacidade máxima = 50 \n Tente  novamente!")
