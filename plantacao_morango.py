def area(comp, larg):
    return comp * larg


comp1 = int(input("Digite o comprimento do primeiro terreno em metros:"))
largura1 = int(input("Digite a largura do primeiro terreno em metros"))

comp2 = int(input("Digite o comprimento do segundo terreno em metros:"))
largura2 = int(input("Digite a largura do segundo terreno em metros:"))

if area(comp1, largura1) > area(comp2, largura2):
    print(area(comp1, largura1))
else:
    print(area(comp2, largura2))
