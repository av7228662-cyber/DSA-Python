# def fun(matrix):
#     n=len(matrix)
#     result=[[0 for _  in range (n)] for _ in range(n)]
#     for i in range(0,n):
#         for j in range(0,n):
#             result[j][(n-1)-i]=matrix[i][j]
#     return result
# x=int(input("enter the row"))
# y=int(input("enter the col"))
# arr=[]

# for i in range(x):
#     row = []
#     for j in range(y):
#         row.append(int(input("Enter the element: ")))
#     arr.append(row)
# print(arr)
# print(fun(arr))




def fun(matrix):
    n=len(matrix)
    for i in range(0,n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(0,n):
        matrix[i].reverse()
    return matrix
x=int(input("enter the row"))
y=int(input("enter the col"))
arr=[]

for i in range(x):
    row = []
    for j in range(y):
        row.append(int(input("Enter the element: ")))
    arr.append(row)
print(arr)
print(fun(arr))