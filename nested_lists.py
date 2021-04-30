list,n_list=[],[]

for _ in range(int(input())):
    for o in range(2):
        list.append(input())
    n_list.append(list)
    list=[]

n_list.sort()
for x in range(0,len(n_list)):
    if n_list[x][1] == n_list[1][1]:
        list.append(n_list[x][0])

list.sort()
[print(x) for x in list]