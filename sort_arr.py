def fun(num):
    n=len(num)
    for i in range(0,n-1):
        if num[i]>num[i+1]:
            return False
    return True
x=int(input("enter the size of array"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))
