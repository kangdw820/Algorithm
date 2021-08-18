a = int(input())

for i in range(a):
    total = 0
    list2 = []
    list1 = map(int, input().split())
    for k in list1:
        if k % 2 == 0:
            list2.append(k)
            total += k
    result = list2[0]
    for j in list2:
        if result >= j:
            result = j
    print(total, result)
