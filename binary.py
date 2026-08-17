#iterative solution

# def fun(num,target):
#     n=len(num)
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if num[mid]==target:
#             return mid
#         elif num[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# x=int(input("enter the arr"))
# arr=[]
# for i in range(x):
#     arr.append(int(input("enter the element")))
# target=int(input("enter the target"))
# print(fun(arr,target))




#recursive solution

# def binary(num,low,high,target):
#     if low>high:
#         return -1
#     mid=(low+high)//2
#     if num[mid]==target:
#         return mid
#     elif num[mid]<target:
#         return binary(num,mid+1,high,target)
#     else:
#         return binary(num,low,mid-1,target)
# x=int(input("enter the number "))
# arr=[]
# for i in range(x):
#     arr.append(int(input("enter the element")))
# t=int(input("enter the target"))
# print(binary(arr ,0,x-1,t))





# lowe bond
def fun(num,target):
    n=len(num)
    low=0
    lb=n
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if num[mid]>target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
x=int(input("enter the number "))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
t=int(input("enter the target"))
print(fun(arr ,t))