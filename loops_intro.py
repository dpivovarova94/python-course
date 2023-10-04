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

# Write a program that shows whether or not the natural number input by the user is a prime number.
# Write you code below
input_number = int(input("Enter a number? "))

count_of_divisors = 0
for i in range(1, input_number + 1):
    if input_number % i == 0:
        count_of_divisors = count_of_divisors + 1

if count_of_divisors == 2:
    print(input_number, "is a prime number")
else:
    print(input_number, "is not a prime number")

# ---------------------------WHILE LOOPS-------------------------------------

# Sometimes, a loop doesn’t have a fixed number of repetitions. Instead, an indicator value stops the loop. This special value is called the sentinel value. For example, we don’t know how much data is in a file without reading it all.
# Write a program that shows the terms of the geometric sequence1,3,9... that stops before the value exceeds 1000
# Write your code here
i = 1
while i < 1000:
    print(i)
    i = i * 3

# The average is calculated by dividing the sum of the values by their number. Write a program that calculates the average of the numbers provided by the user. The program should stop and display the result when the user inputs 0.
# Write your code here
a = 1
sum = 0
count_value = 0
while a!=0:
    a = int(input("Enter a value: "))
    sum = sum + a
    count_value = count_value + 1
print("Average input is: ", sum/(count_value-1))


# Write your code here
first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
HCF = 1

# Write a program that inputs two natural numbers from the user and displays their GCD, also known as the highest common factor (HCF).
i = 1
while i <= max(first_number, second_number):
    if (first_number % i == 0) and (second_number % i == 0):
        # print(i)
        HCF = i
    i = i + 1
print("The greatest common divisor is: ", HCF)


# better solution
a = int (input ("Enter number 1 :"))
b = int (input ("Enter number 2 :"))
while b != 0:
    r = a % b
    a = b
    b = r

print ("The greatest common divisor is:",a)

# ---------------------------NESTED LOOPS-------------------------------------

#  The "\t" tab, which includes multiple spaces. We can use " " to show only one space.

# Write a program that shows the ordered pairs"
# ( 1 , 1 )   ( 1 , 2 )   ( 1 , 3 )   ( 1 , 4 )   ( 1 , 5 )
# ( 2 , 1 )   ( 2 , 2 )   ( 2 , 3 )   ( 2 , 4 )   ( 2 , 5 )
# ( 3 , 1 )   ( 3 , 2 )   ( 3 , 3 )   ( 3 , 4 )   ( 3 , 5 )
# ( 4 , 1 )   ( 4 , 2 )   ( 4 , 3 )   ( 4 , 4 )   ( 4 , 5 )
# ( 5 , 1 )   ( 5 , 2 )   ( 5 , 3 )   ( 5 , 4 )   ( 5 , 5 )
# Write your code below
for i in range(1,6):
    for e in range(1,6):
        print("(", i, ",", e, ")",end = "\t")
    print() # The print statement of the outer loop displays nothing but moves to the next line of the output.

# Write your code here
input_val = int(input("Enter a number: "))


# Write a program that shows a square shape built with asterisks. The number of asterisks on the side of the square is input by the user.
for i in range(1, input_val+1):
    for i in range(1, input_val+1):
        print("*", end="")
    print()
# Write a program that shows a rectanglular shape built with asterisks. The height and width of the rectangle are input by the user.
# Write your code here
first_value = int(input("Enter first val: "))
second_value = int(input("Enter second value: "))

for i in range(first_value):
    for i in range(second_value):
        print("*", end="")
    print()

# Write a program that shows a right triangle built with asterisks. The side length of the right triangle is input by the user.
# Write your code here
a = int(input("Enter a number: "))
for i in range(a + 1):
    print("*" * i)


# Write a program that displays a hollow square built with asterisks. The length of each side of the hollow square shape is input by the user.
# Write your code here
a = int(input("Enter a number: "))
for x in range(a):
    for y in range(a):
        if (x==0 or x==a-1 or y==0 or y==a-1):
            print("*", end="")
        else:
            print(" ", end="")

    print()
