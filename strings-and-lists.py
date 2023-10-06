# Write your code here.
myString = "Educative"
myString = myString[1:9] + "."
print(myString)

# "Educative" -> evitacudE
# Write your code here.
myString = "Educative"
newString = myString[-1]+myString[-2]+myString[-3]+myString[-4]+myString[-5]+myString[-6]+myString[-7]+myString[-8]+myString[-9]
print(newString)


# A palindrome is a sequence of characters that reads the same backward and forward. Write a program that checks if a string is a palindrome. The length of the string is restricted to four or five characters.
# "level" -> Palindrome

inputString = input("Enter something: ")
if inputString[0] == inputString [ -1] and inputString[1] == inputString[-2]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Write your program here.
inputList = [10,20,30,40,50]
sum = inputList[0] + inputList[1] + inputList[2] + inputList[3] + inputList[4]
print(sum)


# Write a program that displays the sum of every two adjacent values in a list.
v=[10,20,30,40,50]
v[0] += v[1]
v[1] += v[2]
v[2] += v[3]
v[3] += v[4]
print(v)

# Write a program that converts a list of single-digit values into a single decimal number. The length of the list is restricted to five values.
# Write your program here.
myList = [1,2,3,4,5]
for i in myList:
    print(i, end="")


# Write a program that checks if a list is a palindrome. The length of the list is restricted to four or five elements.
# Write your program here.
myList = ['ab','cd','ef','cd','ab']
if myList[0] == myList[-1] and myList[1] == myList[-2]:
    print(myList, "is a palindrome")
else:
    print(myList, "is not a palindrome")

# Write a program that reverses the order of elements in a list. The length of the list is restricted to eight values.
v = ['a','e','i','o','u','w','h','y']
newList = [v[-1], v[-2], v[-3], v[-4], v[-5], v[-6], v[-7], v[-8]]
print(newList)



# --------------------------------LIST WITH LOOPS--------------------------
# u = [1,2,3,4,5,6,7,8,9,10,11,12,21,11,10,9,8,7,6,5,4,3,2,1]
# Write your program here.
u = [1,2,3,4,5,6,7,8,9,10,11,12,21,11,10,9,8,7,6,5,4,3,2,1]

flag = 1
for  i in range(1, len(u)//2):
    if u[i] == u[-(i+1)]:
        flag = 0
print(u)
if flag == 0:
    print("is  a palindrome")
else:
    print("is not a palindrome")



# Write a program to sort the array values in ascending order. An array with integer values in it is given, which has to be sorted in the order such that the smallest element is at the start of the array and the greatest is at the end.
# Write a program to check if a list contains the terms of the Fibonacci sequence.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
count = 2
fibFlag = 1
while count < len(fib) and fibFlag == 1:
    if fib[count] != fib[count-2] + fib[count-1]:
        fibFlag = 0
    count += 1
if fibFlag == 0:

    print ("It's not a Fibonacci sequence due to the value", fib[count-1], "at index", count-1)
else:
    print ("Hurrah ... we've got a Fibonacci sequence.")


# Write a program to show the sum of each row of the matrix. The matrix must have two rows and three columns.

# Write your code here
matrix = [[10,20,30],[40,50,60]]
print(matrix)

row1 = matrix[0][0] + matrix[0][1] + matrix[0][2]
row2 = matrix[1][0] + matrix[1][1] + matrix[1][2]
print("Sum of Row1: ", row1)
print("Sum of Row2: ", row2)

# Write a program to show a matrix in the form of rows and columns, then show the sum of each column. The matrix must have five rows and ten columns.
# Write your code here
rows = 5
cols = 10
myList= [[0,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19],[20,21,22,23,24,25,26,27,28,29],[30,31,32,33,34,35,36,37,38,39],[40,41,42,43,44,45,46,47,48,49]]
colsum = [0]*cols # Creating a new list of zeros of size 10

for i in range(rows):
    for j in range(cols):
        colsum[j] = colsum[j] + myList[i][j]

print(colsum)
