# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number


# n is always positive & n is > 1 & whole #

#pseudo code
# define a function that takes in n as a positive integer > 1 X
# for loop using range() starting with 1, ending with n X
# 3 constraints so need possibly 3 conditionals X
# num % 3 ==0, print "Fizz"
# num % 5 ==0, print "Buzz"
# num % 3 ==0 and num % 5 == 0, print "FizzBuzz"
# else print num X


def fizz_buzz (n):
    
    for num in range(1, n):   #<----- will grab all numbers from 1 to n, not including n
        if num % 3 == 0 and num % 5 == 0:    #<----put conditional with most restraint first
            print("FizzBuzz")
        elif num % 3 == 0:   #<---- modulo helps us see if a number is divisible by something
            print ("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz(16)

