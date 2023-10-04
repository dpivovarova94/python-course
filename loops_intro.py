# Write a program that shows the first five odd numbers
for i in [0,2,4,6,8]:
    a = i + 1
    print(a)

# Write a program that shows the first five terms of the harmonic sequence
# Write your code here
for i in [2,4,6,8,10]:
    print ("1/", i)

# Write a program that shows the first five terms of the geometric sequence
# Write your code here
for i in [0, 1, 2, 3, 4]:
    print(3**i)

# Write a program that prints the first 100 positive odd numbers
# Write your code here
for i in range(0,200, 2):
    print(i+1)

# Write a program that prints the terms of the sequence
# Write your code here
for i in range(0,100,5):
    print(i+1)

# Write a program that takes an integer input by the user and prints a multiplication table for the first 20 multiples, as illustrated below.
# Write you code below
a = int(input("enter a number "))
for i in range (1,21):
    print(a*i)

# Write a program that calculates the average of the numbers that have been input by the user. The program first asks the user how many values they want to average. The number of values should be greater than

count_numbers = int(input("how many numbers you will enter? "))
print(count_numbers)
for i in range(1, count_numbers+1):
    print(input("enter a number "))

# Write a program that shows all the factors of a number that have been provided by the user
# Write you code below
input_number = int(input("enter a number: "))
i = 1
while i <= input_number:
    if (input_number % i == 0):
        print(i)
    i = i + 1
