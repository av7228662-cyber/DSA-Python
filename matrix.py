# def fun(num):
#     rows=len(num)
#     col=len(num[0])
#     for i in range(rows):
#         for  j in range(col):
#           print(num[i][j], end=" ")
#         print()
# x=int(input("enter the row"))
# y=int(input("enter the col"))
# arr=[]

# for i in range(x):
#     row = []
#     for j in range(y):
#         row.append(int(input("Enter the element: ")))
#     arr.append(row)
# fun(arr)





# def fun(num):
#     rows=len(num)
#     col=len(num[0])
#     for i in range(0,rows):
#         for  j in range(0,col):
#           if j<=i:
#              print(num[i][j], end=" ")
#         else:
#             print("*", end=" ")
#         print()
# x=int(input("enter the row"))
# y=int(input("enter the col"))
# arr=[]

# for i in range(x):
#     row = []
#     for j in range(y):
#         row.append(int(input("Enter the element: ")))
#     arr.append(row)
# fun(arr)




def fun(num):
    row=len(num)
    col=len(num[0])
    result=[[0]*row for i in range(col)]
    for i in range(0,row):
        for j in range(0,col):
            result[j][i]=num[i][j]
    print(result)
x=int(input("enter the row"))
y=int(input("enter the col"))
arr=[]

for i in range(x):
    row = []
    for j in range(y):
        row.append(int(input("Enter the element: ")))
    arr.append(row)
fun(arr)
