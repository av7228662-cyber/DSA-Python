def fun(num):
    l=float("-inf")
    s=float("inf")
    for i in range(len(num)):
        if num[i]>l:
           s=l
           l=num[i]
        elif num[i]>s and num[i]!=l:
            s=num[i]
    return s
x=int(input("enter the size of array"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))

            



    