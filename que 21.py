a=list(input("enter the number"))
i=0
count=0
while i<len(a):
    count+=1
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    i+=1 
if count == int(a[-1]):
    print("true")
else:
    print("false")