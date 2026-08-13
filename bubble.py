def fun(num):
    n=len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
x=int(input("Enter the size of array: "))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
    fun(arr)
    print(arr)
print("prime number")
for i in arr:
        # if i%2==0:
        #     print(i,end=" ")
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
                
        if count==2:
                    print(i, end=" ")
            

            