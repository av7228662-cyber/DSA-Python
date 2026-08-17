def fun(num,target):
    n=len(num)
    first=-1
    last=-1
    for i in range(0,n):
        if num[i]==target:
            if first==-1:
                first=i
            last=i
    if first==-1:
        return 0
    return last-first+1

x=int(input("enter the list"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the no")))
t=int(input("enter the target"))
print(fun(arr,t))