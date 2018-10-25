def is_prime(num):
    if num <= 3:
        return (False)
    for a in range (2, num):
        if num % a == 0:
            return (False)
            break
        else:
            return (True) 
    
def main():
    
    #4
    num = eval(input("Enter a number:"))
    num_is_prime = is_prime(num)
    print ("Is it a prime number? Result:",num_is_prime)

    
main()
