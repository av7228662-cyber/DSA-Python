def fun(num):
    n=len(num)
    max_count=0
    for i in range(0,n):
        nums=num[i]
        count=1
        while nums + 1 in num:
             count+=1
             nums+=1
        max_count=max(max_count,count)
    return max_count
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the number")))
print(fun(arr))