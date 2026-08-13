def fun(num,target):
    n=len(num)
    for i in range(n):
        if num[i]==target:
            return 1
    return -1
x=int(input("enter the arr"))
arr=[]
for target in range(x):
    arr.append(int(input("enter the element")))
y=int(input("enter the targe"))
result=fun(arr,y)
if result != -1:
    print("element found:" ,result)
else:
    print("not found")