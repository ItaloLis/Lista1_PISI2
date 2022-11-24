quota = int(input())
proxmes = quota
meses = int(input())

for _ in range(1, meses+1):
    mes = int(input())
    if mes > quota:
        proxmes -= mes - quota
    elif mes < quota:
        proxmes += quota - mes

print(proxmes)
