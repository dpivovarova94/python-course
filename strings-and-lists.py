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
