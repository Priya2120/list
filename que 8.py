# Sab Saath Mei

# Ek code likho jo kisi bhi list ke liye yeh output karta hai, 
# ki uss list mei odd numbers, even numbers aur sab numbers ka: - count
    # sum
    # average

# Sample Output

# odd numbers ka count .... hai even numbers ka count .... hai saare numbers ka count .... 
# hai odd numbers ka sum .... hai even numbers ka sum .... hai saare numbers ka sum .... 
# hai odd numbers ka average .... hai even numbers ka average .... 
# hai saare numbers ka average .... hai

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
b=[]
c=[]
i=1
sum=0
s=0
avg=0
count=0
count1=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        b.append(elements[i])
        count+=1
    else:
        c.append(elements[i])
        s=s+elements[i]
        count1+=1
    i=i+1
print(b,"even number",sum)
print(c,"odd number",s)
 
print(b,"even number")
avg = sum/count
print(avg)

print(c,"odd number")
avg = s/count1
print(avg)
