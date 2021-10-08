n = int(input())
lista = []
def add(a, b):
    return a+b

for i in range(n):
    x, y = input().split(',')
    x = int(x)
    y = int(y)
    lista.append(add(x, y))

for x in lista:
    print(x)
    
    
