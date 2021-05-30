# expanded from.
v=int(input("enter a number :"))
b=str(v)
k=len(b)
t=k-1
i=0
while i<len(b):
    code=int(b[i])
    num=(code)*10**t
    print(num,end=" ")
    if i!=len(b)-1:
        print("+",end=" ")
    i=i+1
    t=t-1