# Q: How to find all pairs in an array of integers 
# whose sum is equal to the given number?
# Output: [[11,19], [12,18],[13,17]].

number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
a=[]
k=0
while i<len(n)/2:
    j=1
    while j<len(n):
        if n[i]+n[j]==number:
            k=([n[i],n[j]])
            a.append(k)
        j=j+1
    i=i+1
print(a)