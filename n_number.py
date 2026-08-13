
# QQuestion 1: Write a recursive function to print numbers from 1 to n and then from n to 1.

# def fun(i,n):
#     if i>n:
#         return
#     # print(i)
#     fun(i+1,n)
#     print(i)
# fun(1,5)




# question 2: Write a recursive function to print the sum of numbers from 1 to n.

# def fun(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     fun(sum+i,i+1,n)
# fun(0,1,10)

# question 3: Write a recursive function to return the sum of numbers from 1 to n.


# def fun(sum,i,n):
#     if i>n:
    
#         return sum
#     return fun(sum+i,i+1,n)
# print(fun(0,1,10))

#question 4: Write a recursive function to return the factorial of a number n.

# def fun(n):
#     if n==0 or n==1:
#         return 1
#     return n*fun(n-1)
# x=int(input("Enter a number: "))
# print(fun(x))

#question 5: Write a recursive function to reverse an array.


# def fun(arr,l,r):
#     if l >= r:
#         return
#     arr[l],arr[r]=arr[r],arr[l]
#     fun(arr,l+1,r-1)
# def rev(arr):
#     fun(arr,0,len(arr)-1)
# x=int(input("Enter the size of array: "))
# arr=[]
# for i in range(x):
#     arr.append(int(input("Enter element: ")))
# rev(arr)
# print(arr)



#quesrion 6: Write a recursive function to check if a string is a palindrome.

# def fun(arr,l,r):
#     if l>=r:
#         return True
#     if arr[l]!=arr[r]:
#         return False
#     return fun(arr,l+1,r-1)
# x=input("Enter a string: ")
# if fun(x,0,len(x)-1):
#     print("Palindrome") 
# else:
#     print("Not Palindrome")

# question 6: Write a recursive function to check if a string is a palindrome.


# def fun(arr,l,r):
#     n=len(arr)
#     l=0
#     r=n-1
#     while l<r:
#         if arr[l]!=arr[r]:
#             return False
#         l+=1
#         r-=1
#         return True
# x=input("Enter a string: ")
# if fun(x,0,len(x)-1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#question 7: Write a recursive function to find the nth Fibonacci number.
# def fun(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fun(n-1)+fun(n-2)
# x=int(input("Enter a number: "))
# print(fun(x))


#question 8: Write a recursive function to find the greatest common divisor (GCD) of two numbers.
# def fun(a,b):
#     if b==0:
#         return a
#     else:

#         return fun(b,a%b)
# x=int(input("Enter first number: "))
# y=int(input("Enter second number: "))
# d=fun(x,y)
# print("GCD of",x,"and",y,"is",d)

#question reverse number 
# x=int(input("Enter a number: "))
# count=0;
# while x>0:
#     last_digit=x%10
#     print(last_digit,end="")
#     x=x//10

# #count number of digits in a number
# x=int(input("Enter a number: "))
# count=0
# n=x
# while n>0:
#     count+=1
#     n//=10
# print("Number of digits in",x,"is",count)


# #sum of digits in a number
# x=int(input("Enter a number: "))
# sum=0
# n=x
# while n>0:
#     last_digit=n%10
#     sum+=last_digit
#     n//=10
# print("Sum of digits in",x,"is",sum)