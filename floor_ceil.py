def fun(num,target):
    n=len(num)
    floor=-1
    ceil=-1
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if  num[mid]==target:
            return [num[mid],num[mid]]
        elif num[mid]>target:
            ceil=num[mid]
            high=mid-1
        else:
            floor=num[mid]
            low=mid+1
    return [floor,ceil]
x=int(input("enter the number"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the  element")))
t=int(input("enter the  target"))
print(fun(arr,t))