sing_num, pd_num= input().split(" ")
sing_num = int(sing_num)
pd_num = int(pd_num)
key = [[] for num in range(sing_num)]
ind = [0 for _ in range(sing_num)]
key2 = [[] for num in range(sing_num)]
outd = [0 for _ in range(sing_num)]
for i in range(pd_num):
    input_list = input().split(" ")
    for k in range(len(input_list)):
        input_list[k] = int(input_list[k])
    for j in range(input_list[0] - 1):
        key[input_list[j + 2] - 1].append(input_list[j + 1])
        key2[input_list[j + 1] - 1].append(input_list[j + 2])
        
for n in range(sing_num):
    if key[n]:
        for i in key[n]:
            ind[n] += 1
    if key2[n]:
        for i in key2[n]:
            outd[n] += 1
    
queue = []
result = []
flag = 1

for i in range(sing_num):
    if ind[i] == 0:
        queue.append(i + 1)
        
for i in range(sing_num):
    if len(queue) == 0:
        flag = 0
        break
    val = queue.pop(0)
    result.append(val)
    for k in key2[val - 1]:
        ind[k - 1] -= 1
        if ind[k - 1] == 0:
            queue.append(k)
        
if flag == 0:
    print(0)
else:
    for i in range(len(result)):
        print(result[i])
