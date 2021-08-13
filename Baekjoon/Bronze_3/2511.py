a = input().split()
b = input().split()
Ascore = Bscore = 0
winner = "D"
for i in range(10):
    if int(a[i]) < int(b[i]):
        Bscore += 3
        winner = "B"
    elif int(a[i]) > int(b[i]):
        Ascore += 3
        winner = "A"
    else:
        Ascore += 1
        Bscore += 1
        
print(Ascore, Bscore) 

if Ascore < Bscore: print("B")
elif Ascore > Bscore: print("A")
else: print(winner)
