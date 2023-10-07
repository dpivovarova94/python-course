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
list1 = [2,4,10]
# You are required to use the above variables to find
# the index of the first outlier in the list.
# You may start your code from here to store the correct result in
# the variable idx
idx = 1
flag = 0
if len(list1) < 5:
    idx = 0
    print("The list has less than five elements.", idx)
else:
    while idx < (len(list1)-1) and flag == 0:
        if list1[idx] - list1[idx-1] != list1[idx+1] - list1[idx]:
            flag = 1
        idx += 1
    if flag == 1:
        print("The outlier value is at the index: ", idx)
    else:
        idx = -1
        print("There is no outlier in the list.", idx)
