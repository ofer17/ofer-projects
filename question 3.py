def check(word):
    i=-(len(word))
    x=-2
    nword=word[-1]
    while x>=i:
        nword=str(nword)+str(word[x])
        x = x-1
    if word==nword:
        return True
    else:
        return False
word=input("enter word or number: ")
if check(word):
    print("correct!"+word)
else:
    print("this is not correct")