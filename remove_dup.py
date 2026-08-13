def fun(num):
    n=len(num)
    freq={}
    for i in range(0,n):
        freq[num[i]]=0
    j=0
    for k in freq:
        num[j]=k
        j+=1
    return j
x=int(input("enter the size of array"))
arr=[]
for i in range(x):
    arr.append(int(input("enter the nuum")))
print(fun(arr))