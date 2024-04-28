word= input("enter word or sentence ")
i=-(len(word))
x=-2
nword=word[-1]
while x>=i:
    nword=str(nword)+str(word[x])
    x = x-1
print(nword)