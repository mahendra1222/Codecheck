l1 =[2,3,4,5,3,88,22,99,45,76,12]
# # print(list(str1.split()))
# # print(list(str1))
# n=int(input("Enter a value: "))
# ans=[]
# for i in range(-1,-n-1,-1):
#     ans.insert(0,l1[i])
# print(ans)
# ans.extend(l1[:len(l1)-n])
# print((ans))
# def decor(fun):
#     def inner(a,b):
#         if b==0:
#             return "Oops!!!  con't divide"
#         else:
#             return fun(a,b)
#     return inner
#
#
#
# @decor
# def divide(a,b):
#     return a/b
# print(divide(6,0))
# def flatten(lst):
#     flat_list = []
#     for item in lst:
#         try:
#             flat_list.extend(flatten(item))
#         except:
#             flat_list.append(item)
#     return flat_list
#
# # Example
# multi_dim_list = [1, [2, 3], [4, [5, 6]], 7]
#
# flat_list = flatten(multi_dim_list)
# print(flat_list)

# def Calculations(a,b):
#     sum="Sum of given two numbers is: { }".format(a+b)
#     Multiplication="Multiplication of given two numbers is: { }".format(a*b)
#     return sum,Multiplication
#
#
#
# a=int(input("Enter a,b values : "))
# print(Calculations(a,b))


# def requred(a,b):
#     print("Previous number is {} and Current number is {} and SUM is {}".format(a,b,a+b))
#
#
# for i in range(10):
#     if i==0:
#         b=i
#         a=i
#     else:
#         b=i
#         a=i-1
#     requred(a,b)

# s="CurrentNumber"
# l=list(s)
# for i in range(len(l)):
#     if i%2==0:
#         print(l[i],end=",")
# n=int(input("Enter n value : "))
# print(s[n::])

# s = "Emma is good developer. Emma is a writer"
# q=input("Enter sub string :")
# a=s.count(q)
# print("Given substring was repeated {} time in given string".format(a))

# n=5
# for i in range(1,n+2):
#     print(str(i)*i)

#Palindrome or not
# n=144
# s1=str(n)
# s2=s1[::-1]
# if s1==s2:
#     print("Given number is palindrome")
# else:
#     print("given number is not a palindrome")


# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# def Req(l1,l2):
#     ans=[]
#     for i in l1:
#         if i%2!=0:
#             ans.append(i)
#     for i in l2:
#         if i % 2 == 0:
#             ans.append(i)
#     return ans
# print(Req(list1,list2))


n = 7456
ans = "@"
s = str(n)
l = list(s)
print(l)

# Iterate over the indices of the string in reverse order
for i in range(-1, -len(s) - 1, -1):
    ans = l[i] + ans
    print(ans)

print("Final result:", ans)

#Welcome 













































