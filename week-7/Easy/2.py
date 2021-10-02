a = int(input())
print("Leap Year") if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else print("Not Leap Year")