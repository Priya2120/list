# Yeh image dhyaan se dekhein:
# content

# yeh samajhne ke liye, ki nested_lists mei kaise elements ko access karte hai.
a= [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
s=0
while i<len(a):
    col=0
    while col<len(a):
        s=s+a[i][col]
        col=col+1
        break
    i=i+1
print(s)
x=0
s1=0
while x<len(a):
    row=0
    while row<len(a):
        s1=s1+a[x][row]
        row=row+1
        break
    x=x+1
print(s1)
k=0
s2=0
while k<len(a):
    dig=0
    while dig<len(a):
        if k==dig:
            s2=s2+a[k][dig]
        dig=dig+1
    k=k+1
print(s2)
if s==s1==s2:
    print("it is magic square")
else:
    print("it is not magic square")







