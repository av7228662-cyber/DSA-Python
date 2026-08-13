def fun(num):
    n=len(num)
    max_profit=0
    for i in range(0,n):
        for j in range(i+1,n):
            if num[j]>num[i]:
                p=num[j]-num[i] 
                max_profit=max(max_profit,p)
    return max_profit
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))