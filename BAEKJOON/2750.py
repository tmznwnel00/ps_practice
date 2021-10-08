n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))

def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]

selection_sort(lista)

for x in lista:
    print(x)
        
