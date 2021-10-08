num = int(input(""))
i = 1
dic = {}
graph = [[] for j in range(num)]
ind = [0 for j in range(num)]


for j in range(num):
    lis = input("").split(" ")
    dic[i] = int(lis[0])
    k = 1
    while 1:
        if lis[k] == "-1":
            break
        graph[int(lis[k]) - 1].append(i)
        ind[i - 1] += 1
        k += 1
    i += 1
    

queue = []
for j in range(num):
    if ind[j] == 0:
        queue.append(j + 1)

result = [0 for j in range(num)]
for j in range(num):
    result[j] = dic[j + 1]
    
for j in range(num):
    val = queue.pop(0)
    for x in graph[val - 1]:
        result[x - 1] = max(result[x - 1], result[val - 1] + dic[x])
        ind[x - 1] -= 1

        if ind[x - 1] == 0:
            queue.append(x)

for j in range(len(result)):
    print(result[j])


