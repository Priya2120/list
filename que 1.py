# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which 
# numbers are not present in the second array.
# Output: [4, 5]


list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 
i=0
a=[] 
while i<len(list1):
    b=list1[i]
    if b not in list2:
        a.append(b)
    i=i+1
print(a)









    



    