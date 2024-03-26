def print_up_to(n):
    """Print every natural number up to n, inclusive.

    >>> print_up_to(5)
    1
    2
    3
    4
    5
    """
    i = 1
    if i > n:
        return
    else:
        print(i)
        i += 1
        print_up_to(n)





import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)