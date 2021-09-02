one = map(int,input().split())
one = list(one)
two = map(int,input().split())
two = list(two)
three = map(int,input().split())
three = list(three)
def playing(a):
    num = 0
    for i in a:
       num += i
    if num == 0: print("D")
    elif num == 1: print("C")
    elif num == 2: print("B")
    elif num == 3: print("A")
    elif num == 4: print("E")
        
playing(one)
playing(two)
playing(three)
