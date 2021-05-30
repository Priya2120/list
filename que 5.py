# Kitne Aadmi The

# Ek code likho jo kisi bhi list ke liye yeh output karta hai, 
# ki uss list mei kitne odd numbers hai aur kitne even numbers hai.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=[]
c=[]
i=1
while i<len(elements):
    if elements[i]%2==0:
        b.append(elements[i])
    else:
        c.append(elements[i])
    i=i+1
print(b,"even number")
print(c,"odd number")