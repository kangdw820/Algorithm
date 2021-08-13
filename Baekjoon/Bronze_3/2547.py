list1 = []
a = int(input())

for i in range(a):
    input()
    num1 = num2 = num3 = 0
    num1 = int(input())
    for j in range(num1):
        num2 = int(input())
        num3 += num2
    if num3 % num1 == 0:
        list1.append(1)
    else: list1.append(0)

for k in range(a):
    if list1[k] == 0:
        print("NO")
    else: print("YES")
