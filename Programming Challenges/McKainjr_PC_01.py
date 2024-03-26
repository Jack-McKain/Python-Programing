_author_ = "Jack McKain"
_credits_ = ["https://www.geeksforgeeks.org/videos/greedy-algorithm-for-egyptian-fraction/"]
_email_ = "mckainjr@mail.uc.edu"
    

def egypt(p, q):
    """
    >>> egypt(3,4)
    '1/2 + 1/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12'

    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """

    # Base case
    if p == 1:
        return f'1/{q}'

    # Find smallest integer
    n = q // p + 1

    # Recursively call egypt to handle the remaining fraction (p/q - 1/n)
    remaining_p = p * n - q
    remaining_q = q * n

    # Simplify the remaining fraction
    gcd = find_gcd(remaining_p, remaining_q)
    remaining_p //= gcd
    remaining_q //= gcd

    return f'1/{n} + ' + egypt(remaining_p, remaining_q)

def find_gcd(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return find_gcd(b, a % b)


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)