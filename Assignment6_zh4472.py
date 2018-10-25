# CS 303E Assignment 6_Zhaoyi Huang (UTEID:zh4472)

import math

# 1. Write a function to reverse a string.
def reverse_string(string):
    reverse_string = ""
    i = 1
    while i < (len (string) + 1):
        reverse_string = reverse_string + string[-i]
        i += 1
    return reverse_string

# 2&3. Determine whether a word is palindrome
def palindrome(word):
    reverse_word = reverse_string(word)
    if word == reverse_word:
        return (True)
    elif word != reverse_word:
        return (False)

# 4.
def is_prime(num):
    # quick test to test small numbers
    if num <= 3:
        return (True)
    elif num % 2 == 0:
            return (False)
    sqr = int(math.sqrt(num)) + 1
    for a in range(3, sqr, 2):
        if num % a == 0:
            return False
    return True

def main():
    
    # problem 1: Reverse string
    string = input("Enter a string:")
    reversed_string = reverse_string (string)
    print ("Reversed string is:", reversed_string)
    
    # problem 2: Palindrome set up
    word = input("Enter a word to see if it's palindrome:")
    palindrome_test = palindrome(word)
    print ("Result is:",palindrome_test)

    # problem 3: Palindrome test
    times = 1
    while times <=3:
        word_2 = input("Enter a word:")
        palindrome_word_2 = palindrome(word_2)
        if palindrome_word_2 is True:
            print ("Palindrome!")
        else: print ("Not a palindrome.")
        times += 1

    # problem 4: prime number?
    num = eval(input("Enter a number:"))
    num_is_prime = is_prime(num)
    print ("Is it a prime number? Result:",num_is_prime)

    # problem 5: Emirp
    # prompt 3 times
    j = 1
    while j <=3:
        num_e = eval(input("Enter a number:"))
        # see if it's a prime number
        num_e_prime = is_prime(num_e)
        if num_e_prime is True:
            # see if it's a palindrome
            num_e_palin = palindrome (str(num_e))
            if num_e_palin == True:
                print ("Not an emirp.")
            else:
                # see if its reverse is also a prime?
                reverse_num_e = reverse_string (str(num_e))
                reverse_num_e_prime = is_prime (int(reverse_num_e))
                if reverse_num_e_prime == True:
                    print ("Emirp!")
                else: print ("Not an emirp.")
        elif num_e_prime is False:
            print ("Not an emirp.")
        j += 1

    # problem 6: Twin Primes
    i = 2 #because 1 is not a prime number, so we start at 2
    while i < 1000:
        num_a = i
        # see is num_a is a prime number:
        num_a_p = is_prime (num_a)
            # if num_a is a prime number, see if its twin prime exists
        if num_a_p == True:
            num_b = num_a + 2 # twin number
            # see if twin number is prime
            num_b_p = is_prime (num_b) 
            if num_b_p == True:
                print (str(num_a)+","+str(num_b))
        i += 1
        
main()


