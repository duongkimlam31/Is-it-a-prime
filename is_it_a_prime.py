# a function that takes in an integer to determine whether it is a prime number or not
def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
