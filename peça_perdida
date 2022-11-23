def somalist(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


def metodo(quantidade_de_pecas, lista_incompleta):
    total_lista_completa = int((quantidade_de_pecas * (quantidade_de_pecas + 1)) / 2)
    total_lista_incompleta = somalist(lista_incompleta)
    print(total_lista_completa - total_lista_incompleta)


def main():
    quantidade_de_pecas = int(input())
    lista_incompleta = [int(i) for i in input().split()]
    metodo(quantidade_de_pecas, lista_incompleta)


main()
