#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, word):
        self.index = 0
        self.word = word

    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        letter = self.word[self.index]
        self.index += 1
        return f"Give me an {letter}"

    def __iter__(self):
        return self


#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    
    "*** YOUR CODE HERE ***"
    
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            number = self.current
            self.current -= 1
            return number


##############
# Generators #
##############

# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)
    <class 'generator'>
    
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    
    n=2
    while True:
        yield n
        n += 2

#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    
    for item in s:
        yield item * k

def naturals():
    n = 1
    while True:
        yield n
        n += 1


# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

    while n >= 0:
        yield n
        n -= 1

# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    
    while n >= 1:
        yield n
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    
    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)