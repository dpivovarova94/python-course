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

num = int(input("Enter number: ")) # The variable test_value contains the value to be tested.
pwr = 0 # The variable to store the result calculated with the help of num.
# You are required to calculate the value of pwr as
# the power of 2 nearest to the num.
# You may start your code from here onwards.
# Assume that the variable test_value is already defined.
# num = test_value # The variable test_value contains the value to be tested.

i = 0
pwr = 2 ** i # Calculating power before while loop
lastpower = 0

while(pwr < num):# Checking the power should be less than the num
    lastpower = pwr # Assigning last power
    i+=1
    pwr = 2 ** i # Calculating next power
    print("pwr ", pwr)
    print("lastpower: ", lastpower)
    print("i ", i)

# Checking difference between the num and the both powers
diff1 = num - lastpower
diff2 = pwr - num
#If the difference between power and number is greater than or equal to
#the difference between last power and the number then store lastpower in pwr.
if diff2 >= diff1:
    pwr = lastpower
print("The",pwr,"is the power of 2 nearest to", num)
