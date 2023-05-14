import random

dice1=random.randint(1,6)
dice2=random.randint(1,6)
dice3=random.randint(1,6)

print(dice1, dice2, dice3)

if dice1==dice2==dice3:
    prize1=10000+(dice1*1000)
    print(prize1)

if dice1==dice2!=dice3:
    prize2=1000+(dice1*100)
    print(prize2)

if dice1==dice3!=dice2:
    prize3=1000+(dice1*100)
    print(prize3)

if dice2==dice3!=dice1:
    prize4=1000+(dice2*100) 
    print(prize4)   
        
if dice1!=dice2!=dice3:
    if dice1>dice2 and dice1>dice3:
        print(dice1*100)
    if dice2>dice1 and dice2>dice3:
        print(dice2*100)
    if dice3>dice1 and dice3>dice2:
        print(dice3*100)