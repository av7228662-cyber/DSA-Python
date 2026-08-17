# def fun(num):

#     n=len(num)
#     mini=float("inf")
#     for i in range(0,n):
#         mini=min(mini,num[i])
#     return mini
# x=int(input("enter the no."))
# arr=[]
# for i in range(x):
#     arr.append(int(input("enter the element")))
# print(fun(arr))



def fun(num):
    n=len(num)
    low=-1
    high=n-1
    mini=float("inf")
    while low<=high:
        mid=(low+high)//2
        if num[mid]<=num[high]:
            mini=min(mini,num[mid])
            high=mid-1
        else:
            mini=min(mini,num[low])
            low=mid+1
    return mini

x=int(input("enter the no."))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))

    