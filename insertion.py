def fun(num):
    n=len(num)
    for i in range(1,n):
        key=num[i]
        j=i-1
        while j>=0 and key<num[j]:
            num[j+1]=num[j]
            j-=1
        num[j+1]=key
x=int(input("Enter the size of array: "))
arr=[]
for i in range(x):
    arr.append(int(input("enter the element")))
fun(arr)
print("Sorted array is:", arr)