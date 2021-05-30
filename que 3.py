# Yeh kisi student ke peechle teen saal ke marks hai. 
# Aap ko jitne bhi saal hai, har saal ke average marks print karne hai. 
# Jaise, uppar wali list ka output yeh hona chahiye:

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
sum=0
while i<len(marks):
    j=0
    s=0
    while j<len(marks[i]):
        s=s+marks[i][j]     
        j=j+1
    sum=sum+s           
    i=i+1  
print(sum)
avg = sum/15
print(avg)

    

    


