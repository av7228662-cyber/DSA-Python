# bruteforce solution
# def fun(num):
#     n=len(num)
#     my_set=set()
#     for i in range(0,n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for l in range(k+1,n):
#                     if num[i]+num[j]+num[k]+num[l]==0:
#                         temp=[num[i],num[j],num[k],num[l]]
#                         my_set.add(tuple(temp))
#     return [list(ans) for ans in my_set]
# x=int(input("enter the arr"))
# arr=[]
# for i in range(x):
#     arr.append(int(input("enter the element")))
# print(fun(arr))





# better solution

def fun(num):
    result=set()
    n=len(num)
    for i in range(n):
        my_set=set()
        for j in range(i+1,n):
            for k in range(j+1,n):
                fourth=-(num[i]+num[j]+num[k])
                if fourth in my_set:
                    temp=[num[i],num[j],num[k],fourth]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(num[k])
    return [list(ans) for ans in result]
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))
            
