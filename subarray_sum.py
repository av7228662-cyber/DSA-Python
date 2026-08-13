def fun(num):
    n=len(num)
    maxi=float("-inf")
    for i in range(0,n):
        total=0
        for j in range(i,n):
            total=total+num[j]
            maxi=max(maxi,total)
    return maxi
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))