# Write your code below
def showTableOf4():
    for i in range(1,21):
        print("4 *", i, end="" )
        print(" = ", end="" )
        print(4 * i)

showTableOf4()

# Write a function that checks if a string or character is present in the list. If it’s present, display its index in the list. Call your function to display the results.



def findString(string, list1):
    flag = 0
    i = 0
    lp = len(list1)

    while i < lp:
        if list1[i] == string:
            flag = 1
            print(string," is found at index", i)
        i += 1
    if flag == 0:
        print(string, "is not found in the list")

list1 = ['2','55','888','9','30','45']
string = input("Enter a string: ")
findString(string, list1)

# Write a function, fibo(), that receives the parameter n to specify the number of terms of the Fibonacci sequence. That function will return a list containing the sequence.
def fibo(n):
    # generate a fibonacci sequence
    fib = [0]*n
    if n in {0,1}:
        fib[n] = n
    else:
        fib[n] = fibo(n - 1) + fibo(n - 2)

n = 10
print("First ", n, "terms of fiboncci sequence are: ")
print(fibo(10))
