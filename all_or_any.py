x = int(input())
input_string = input()
list  = input_string.split()
count,counts = 0,0
for x in list:
    a=b=int(x)
    rev=0
    while(a>0):
        dig=a%10
        rev=rev*10+dig
        a=a//10
    if b == rev:
        count+=1
    else:
        pass

for t in list:
    if int(t) > 0:
        counts+=1
    else:
        pass

if (counts==len(list)) and count>=1:
    print("True")
else:
    print("False")
