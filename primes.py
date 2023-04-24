import math

def get_gcf(n1, n2):
    '''Returns the gcf of 2 positive ints
    Returns 0 if there are no common factors. 
    '''
    common_prime_factors = set(get_prime_factors(n1)).intersection(set(get_prime_factors(n2)))
    return (math.prod(common_prime_factors)
            if len(common_prime_factors) != 0 else 0)


def get_prime_factors(n):
    """Returns a list of the factors of int n
    n = positive int
    Uses factor tree
    """
    if is_prime(n):
        return [n]

    # it shouldn't matter which prime factor
    prime_factor = min(get_lesser_primes(n), key=lambda i: n % i)
    return [prime_factor] + get_prime_factors(n // prime_factor)


def get_primes_in_range(x, y):
    """Returns a list of all primes in the range x, y
    x = positive integer, less than y
    y = positive integer, greater than x
    """
    # this could be made for efficient by using the sieve of 
    # Eratosthenes, and starting the inner loop at x rather than 2

    x_primes = get_lesser_primes(x)
    y_primes = get_lesser_primes(y)

    for i in x_primes:
        if i in y_primes:
            y_primes.remove(i)
    
    return y_primes


def get_lesser_primes(n):
    """Returns a list of all prime numbers < n.
    n = positive integer
    Uses the Sieve of Eratosthenes
    """
    if n == 1:
        return []
    lesser_nums = [*range(2, n)]
    for i in lesser_nums:
        if is_prime(i):
            for k in lesser_nums:
                if k % i == 0 and k != i:
                    lesser_nums.remove(k)
    return lesser_nums

def is_prime(n):
    """Returns true if n is prime, false otherwise."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
    return True

print(get_gcf(206, 159))
