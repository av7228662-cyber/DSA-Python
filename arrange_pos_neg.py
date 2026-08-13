# def fun(num):
   
#     pos=[]
#     neg=[]
#     for i in range(len(num)):
#         if num[i]>=0:
#             pos.append(num[i])
#         else:
#             neg.append(num[i])

#     for i in range(0,len(pos)):
#         num[2*i]=pos[i]
#         num[(2*i)+1]=neg[i]
#     return num
# x=int(input("enter the arr")) 
# arr=[]
# for i in range(x):
#     arr.append(int(input("enter the element")))
# print(fun(arr)


 # optimal solution



def fun(num):
    n=len(num)
    pos=0
    neg=1
    result=[0]*n
    for i in range(0,n):
        if num[i]>0:
            result[pos]=num[i]
            pos+=2
        else:
            result[neg]=num[i]
            neg+=2
    return result
x=int(input("enter the arr")) 
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
print(fun(arr))