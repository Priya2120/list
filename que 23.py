a=[]
i=0
print(a)
while i<len(a):
    j=0
    while j<i:
        if a[i]<a[j]:
            temp=[i]
            a[i]=temp
        j=j+1
    i=i+1
print(a)