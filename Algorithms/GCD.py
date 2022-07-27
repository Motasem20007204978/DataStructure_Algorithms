
# gcd is the greatest common divisor of two numbers
# the greatest common divisor of two numbers is the largest number that divides both of them
# the gcd is very important in cryptography
# the gcd is used to find the multiplicative inverse of a number
# the multiplicative inverse of a number is the number that multiplies the number to be inversed with the modulus of the number
# it has arelation with prime numbers

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(357,234))
# the running time is O(log(a*b))
# the complexity of 100 digits number is about 600 
