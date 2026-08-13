# Question 1 selection sort using recursion

def selection_sort(num):
    n=len(num)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]

x=int(input("Enter the size of array: "))
arr=[]
for i in range(x):
    arr.append(int(input("Enter element: ")))
selection_sort(arr)
print(arr)
print("prime numbers:")
    # for i in arr:
    #  if i%2==0:                      for even numbers in sorrted array :

    #       print(i,end=" ")
for i in arr:
    count = 0
    for j in range(1, i + 1):         # for prime numbers in sorted array:
        if i % j == 0:
            count += 1

    if count == 2:
        print(i , end=" ")