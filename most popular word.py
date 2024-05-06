sen=input("enter a sentence: ")
sen=sen.split()
def f(sen):
    d={}
    for word in sen:
        if word in d:
            d[word] +=1 
        else:
            d[word]=1
    popular=sorted(d.items(), key=lambda x: x[1])
    popular.reverse()
    N=int(input("how many word you want to know? "))
    if N<=len(popular) and N>0:
        for i in range(N):
            print("the word: "+popular[i][0]+" shows "+str(popular[i][1])+" times")
    else:
        print("Error")
f(sen)   