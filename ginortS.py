lower_case,uppercase_case,odd_num,even_num = [],[],[],[]
for y in input():
    if (y.islower()):
        lower_case.append(y)
    elif (y.isupper()):
        uppercase_case.append(y)
    else:
        if int(y)%2==0:
            even_num.append(y)
        else:
            odd_num.append(y)

lower_case.sort()
uppercase_case.sort()
even_num.sort()
odd_num.sort()

[print(str(r),end="") for r in (lower_case + uppercase_case + odd_num + even_num)]
print("\n")


