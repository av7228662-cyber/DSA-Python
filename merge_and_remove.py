def fun(num1, num2):
    n = len(num1)
    m = len(num2)
    num1.sort()
    num2.sort()
    i = 0
    j = 0
    result = []

    while i < n and j < m:
        if num1[i] < num2[j]:
            if len(result) == 0 or result[-1] != num1[i]:
                result.append(num1[i])
            i += 1

        elif num1[i] > num2[j]:
            if len(result) == 0 or result[-1] != num2[j]:
                result.append(num2[j])
            j += 1

        else:
            if len(result) == 0 or result[-1] != num1[i]:
                result.append(num1[i])
            i += 1
            j += 1

    while i < n:
        if len(result) == 0 or result[-1] != num1[i]:
            result.append(num1[i])
        i += 1

    while j < m:
        if len(result) == 0 or result[-1] != num2[j]:
            result.append(num2[j])
        j += 1

    return result


x = int(input("Enter size of array1: "))
arr1 = []

for i in range(x):
    arr1.append(int(input("Enter element: ")))

y = int(input("Enter size of array2: "))
arr2=[]
for i in range(y):
    arr2.append(int(input("Enter element: ")))

print(fun(arr1, arr2))