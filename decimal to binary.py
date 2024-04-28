def binary():
    i=7
    bin=[0]*8
    num=int(input("enter number "))
    while i>=0:
        if num%2==0:
            bin[i]=0
            num=num/2
        else:
            bin[i]=1
            num = num-1
            num=num/2
        i =i-1
    i=0
    while i<=7:
        if bin[i]==0:
            bin[i]=1
            i=i+1
        else:
            bin[i]=0
            i=i+1
    i=7
    while bin[i]==1:
        bin[i]=0
        if bin[i-1]==0:
            bin[i-1]=1
        else:
            i=i-1
    return(bin)
print(binary())