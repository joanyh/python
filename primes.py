


def is_prime(num):
    """
    This is a function that takes as its input an integer.
    It returns True if the number if prime and False if the
    number is composite.
    """

    # Quick test for small prime numbers
    if num <= 3:
        return True

    # Quick test for even numbers
    for a in range (2, num):
        if num % a == 0:
            return False
         
    # Implement an algorithm below to test for primes,
    # e.g. Sieve of Eratosthenes


 
# Example numbers to test:

assert is_prime(1) == True
assert is_prime(10) == False
assert is_prime(15) == False
assert is_prime(150000003) == False

 
