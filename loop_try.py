# num = 23
# gum = 1
# while (num > 0):
#    gum = num % 10
#    num //= 10
#    print(gum)
#    print(num)
# print(gum)

# first loop: gum = 3, num = 2
# second loop: gum = 2 % 10 = 2
# Write your code here.
# string_input = "Educative"
# print (string_input[-1])
# print (string_input[-2])
# print (string_input[-3])
# print (string_input[-4])
# print (string_input[-5])
# print (string_input[-6])
# print (string_input[-7])
# print (string_input[-8])
# print (string_input[-9])

# inputString = input("Enter something: ")
# if inputString[0] == inputString [ -1] and inputString[1] == inputString[-2]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# v = ['a','e','i','o','u','w','h','y']
# newList = [v[-1], v[-2], v[-3], v[-4], v[-5], v[-6], v[-7], v[-8]]
# print(newList)
# a = ['a','b','c','d','e','f','g','h','i']
# i = 1
# while (i < len(a)):
#    print(a[-i], end=' ')
#    i += 2

# Assume that the following variable is already defined:
# list1 = [5,8,11,13,17]
# list1 = [2,4,10]

# # You are required to use the above variables to find
# # the index of the first outlier in the list.
# # You may start your code from here to store the correct result in
# # the variable idx
# idx = 1
# flag = 0
# if len(list1) < 5:
#     idx = 0
#     print("The list has less than five elements.", idx)
# else:
#     while idx < (len(list1)-1) and flag == 0:
#         if list1[idx] - list1[idx-1] != list1[idx+1] - list1[idx]:
#             flag = 1
#         idx += 1
#     if flag == 1:
#         print("The outlier value is at the index: ", idx)
#     else:
#         idx = -1
#         print("There is no outlier in the list.", idx)

# def findString(string, list1):
#     flag = 0
#     i = 0
#     lp = len(list1)

#     while i < lp:
#         if list1[i] == string:
#             flag = 1
#             print(string," is found at index", i)
#         i += 1
#     if flag == 0:
#         print(string, "is not found in the list")

# list1 = ['2','55','888','9','30','45']
# string = input("Enter a string: ")
# findString(string, list1)
# def fibo(n):
#     # generate a fibonacci sequence
#     if n in {0,1}:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
    
# n = 10
# fib_list = [0] * n
# count = 0
# while count < n:
#     fib_list[count] = fibo(count)
#     count += 1

# print("First ", n, "terms of fiboncci sequence are: ")
# # print(fib_list)

# # # print(sorted("aAbB"))
# # # msg = 'good at work at night'
# # # print(msg.find('at'))
# # # print('a2H'.iss())
# # # print("Hello".lower())
def checkAnagrams(str1, str2):
    num = 0
    flag = 0
    sum = 0

    if len(str1) == len(str2):
        # write code
        str1 = str1.lower()
        str2 = str2.lower()
        i = 0

        while i < len(str1):
            # while flag != 1:
            if str1[i] in list(str2):
                flag = 0
            else:
                flag = 1
            sum += flag
            i += 1
            # print(sum)
        if sum == 0:
            num = 1
        else:
            num = -1
    else:
        num = -1
    return num

print(checkAnagrams("accept", "expect"))
print(checkAnagrams("Skin", "sink"))


# str1 = "skin"
# str2 = "sink"
# i = 0

# # while i < len(str1):
# #     if str1[i] in str2.split():
# #       print(str1[i])
# #       print(str2.split())
# #     i +=1

# print(str1[1])
# print(list(str2))