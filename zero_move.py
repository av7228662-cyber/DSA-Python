def fun(num):
    n=len(num)
    j=0
    for i in range(n):

        if num[i]!=0:
            num[j]=num[i]
            j+=1
    while j<n:
        num[j]=0
        j+=1
    return num
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))