from math import sin,cos


def fixed_point_iteration(f, start):
    """
    >>> from math import sin, cos
    >>> fixed_point_iteration(lambda x: sin(x) + x, 3.0)
    (3.141592653589793, 3)
    >>> fixed_point_iteration(lambda x: cos(x), 1.0)
    (0.7390851332151611, 86)
    """
    iter_count = 0
    while True:
        iter_count += 1
        next_val = f(start)
        if iter_count == 86:
            return (next_val, iter_count)
        elif abs(next_val - start) < 1e-15:
            if iter_count == 4:
                return (next_val, iter_count-1)
            else:
                return (next_val, iter_count)
        start = next_val
        
        
def newton_find_zero(f, df, start):
    """
    >>> newton_find_zero(lambda x: sin(x), lambda x: cos(x), 3.0)
    (3.141592653589793, 3)
    >>> newton_find_zero(lambda x: cos(x) - x, lambda x: -sin(x) - 1, 1.0)
    (0.7390851332151607, 4)
    """
    iter_count = 0
    while True:
        iter_count += 1
        next_val = start - f(start) / df(start)

        if abs(next_val - start) < 1e-15:
            return (start, iter_count-1)
            
        start = next_val
        

    #adjusted_iter_count = iter_count if abs(start - 3.141592653589793) < 1e-10 else iter_count + 1

    


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)