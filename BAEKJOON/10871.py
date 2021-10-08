a, b = input().split()
a = int(a)
b = int(b)
c = input().split()
c = list(map(int, c))
for i in c:
    if i < b:
        print(i, end = ' ')

