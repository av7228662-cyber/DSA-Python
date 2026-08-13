
#question 1 rotate array



# def fun(num):
#     n=len(num)
#     temp=num[n-1]
#     for i in range(n-2,-1,-1):
#         num[i+1]=num[i]
#     num[0]=temp
#     return num
# x=int(input("enter arr"))
# arr=[]
# for i in range(x):
#     arr.append(int(input("enter the number")))
# print(fun(arr))




#Question 2 Rotate array in k times



def fun(num,k):
    n=len(num)
    rotation=k%n
    for _ in range(0,rotation):
        e=num.pop()
        num.insert(0,e)
    return num
x=int(input("enter the arr"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
k=int(input("enter the rotation"))
print(fun(arr,k))