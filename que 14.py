# Remove Substring
# Aapko aisa program likhna hai, jo subStr ki saari occurences 
# ko mainStr se hata degi. Yaani uppar wale program ka output yeh hoga:


# s = ("the quick brown fox jumped over the lazy dog. the dog slept over the verandah.")
# l = s.split()
# k = []
# for i in l:
#     if (s.count(i)>1 and (i not in k)or s.count(i)==1):
#         k.append(i)
# print(' '.join(k))



a="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
b=a.split()
i=0
while i<len(b):
    if b[i]=="over":
        i+=1
        continue
    print(b[i],end=" ")
    i=i+1