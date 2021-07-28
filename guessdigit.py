import random
r=random.randint(1,100)
sum=0
for x in range(100):
    n=int(input("guess the number bw 1 to 100 :\t"))
    if n>r:
        print("too high")
        sum+=1
    elif n<r:
        print("too low")
        sum+=1
    else:
        break
print("well done!!! Done in attempts:",sum+1)