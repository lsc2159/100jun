N=int(input())
d3=N
count=0

while True:
    d1=(d3//10)+(d3%10)
    d2=((d3%10)*10)+(d1%10)
    count +=1
    
    if d2==N:
        break
    d3=d2
print(count)