a = int(input())
m = int(input())

if a <= 50 and m <= 50:
    if a + m <= 50:
        print("S")
    else:
        print("N")
else:
    print("Capacidade máxima = 50 pessoas")
