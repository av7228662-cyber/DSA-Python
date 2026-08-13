def fun(num):
    n=len(num)
    my_set=set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if num[i]+num[j]+num[k]==0:
                    temp=[num[i],num[j],num[k]]
                    temp.sort()
                    my_set.add(tuple(temp))     
    return [list(ans) for ans in my_set]
x=int(input("enter the number"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the number")))
print(fun(arr))