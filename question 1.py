def is_first(num):
    if num<=1:
        return False
    elif num<=3 or num==5:
        return True
    elif num/2>1 and num%2==0:
        return False
    elif num/3>1 and num%3==0:
        return False
    elif num/5>1 and num%5==0:
        return False
    elif num/num==1 and num%num==0:
        return True
start=int(input("enter the first number plase: "))
end=int(input("enter the last number plase: "))
for x in range(start,end+1):
    if is_first(x):
        print(x)