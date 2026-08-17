# def fun(num,target):
#     n=len(num)
#     temp=num[n-1]
#     for i in range(n-2,-1,-1):
#          num[i+1]=num[i]
#          num[0]=temp
#          return num
#     for i in range(0,n):
#         if num[i]==target:
#             return i
#     return -1
# x=int(input("enter the no."))
# arr=[]
# for i in range(x):
#     arr.append(int(input("enter the element")))
# t=int(input("enter the target"))
# print(fun(arr,t))



#optimal solution


def fun(num,target):
    n=len(num)
    low=-1
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if num[mid]==target:
            return mid
        if num[mid]<=num[high]:
            if num[mid]<= target<=num[high]:
                low=mid+1
            else:
             high=mid-1
        else:
         num[i]<=target<=num[mid]
        high=mid-1
    else:
            low=mid+1
    return num 
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
t=int(input("enter the target"))
print(fun(arr,t))