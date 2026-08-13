def fun(num,target):
    n=len(num)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if num[i]+num[j]==target:
                return [i,j]
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the number")))
y=int(input("enter the target"))
print(fun(arr,y))