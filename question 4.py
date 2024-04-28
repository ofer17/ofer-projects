sen=input("enter a sentence: ")
sen=sen.split()
word=sen[0]
for x in range(1,len(sen)):
    if len(word)<len(sen[x]):
        word=sen[x]
print(word)

