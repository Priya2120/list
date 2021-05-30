# Average Kitna Hai

# Ek code likho jo kissi bhi list ke liye uss list ke do average ko output karta hai, 
# ki uss list mei odd numbers ka average aur even numbers ka average kitna hai.


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
print(b,"even number")
avg = sum/count
print(avg)

print(c,"odd number")
avg = s/count1
print(avg)