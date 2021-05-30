# Count Occurences

# Occurences - occur shabd se bana hai, jiska matlab hota hai, 
# ki kitni baar aata hai. Sample List

# Sample List ka Output:
 
# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]
 

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
k=[]
i=0
while i<len(char_list):
    j=0
    count=0
    a=[]
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    a.append(char_list[i])
    a.append(count)
    if a not in k:
        k.append(a)
    i=i+1
print(k)
    

# names = ["a", "n", "t", "a", "a", "t"]
# nm=input("enter name to count :")
# count=names.count(nm)
# print("count",count)






        
