a = int(input())
same = a
i = 0

while 1:
    if a < 10:
        b = a*10
        b = str(b)
        a = str(a)
        result = a + b[0]
        a = int(result)
        
    else:
        a = str(a)
        num1 = int(a[0])
        num2 = int(a[1])
        b = num1 + num2
        if b < 10:
            result1 = b*10
            result1 = str(result1)
            result2 = a[1] + result1[0]
            a = int(result2)
            
        else:
            b = str(b)
            a = str(num2) + b[1]
            a = int(a)
            
    i += 1
    
    if same == a:
        print(i)
        break
            
