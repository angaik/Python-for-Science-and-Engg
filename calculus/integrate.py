"""
This module contains functions to numerically integrate functions over a domain.
"""

def midpt(x_start,x_end,f):
    """
    Args:
        x_start (float) : Starting point.
        x_end (float) : Ending point.
        f (Callable) : A function
    """
    return (x_end-x_start)*f((x_start+x_end)/2)

def comp_midpt(x_start:float,x_end:float,step_size:float,f):
    """
    Args:
        x_start (float) : Starting point.
        x_end (float) : Ending point.
        step_size (float) : Step size
        f (Callable) : A function
    """
    result = 0
    x_init = x_start
    while x_init <= x_end:
        x_next = x_init + step_size
        result += midpt(x_init,x_next,f)
        x_init = x_next
    return result     

def trapezoidal(x_start,x_end,f):
    """
    Args:
        x_start (float) : Starting point.
        x_end (float) : Ending point.
        f (Callable) : A function
    """
    return (x_end-x_start)*((f(x_start)+f(x_end))/2)

def comp_trapezoidal(x_start,x_end,step_size,f):
    """
    Args:
        x_start (float) : Starting point.
        x_end (float) : Ending point.
        step_size (float) : Step size
        f (Callable) : A function
    """
    result = 0
    x_init = x_start
    while x_init <= x_end:
        x_next = x_init + step_size
        result += step_size * (f(x_init) + f(x_next))/2
        x_init = x_next
    return result

def simpson_13(x_start,x_end,step_size,f):
    """
    Args:
        x_start (float) : Starting point.
        x_end (float) : Ending point.
        step_size (float) : Step size
        f (Callable) : A function
    """
    f_intermediate=f((x_start+x_end)/2)
    return (step_size/3)*(f(x_start)+4*f_intermediate+f(x_end))

def comp_simpson_13(x_start,x_end,step_size,f):
    result = 0
    x_init = x_start
    while x_init <= x_end:
        x_next = x_init + step_size
        result += simpson_13(x_init,x_next,step_size,f)
        x_init = x_next
    return result

if __name__ == "__main__":
    # Numerical Integration of f(x) = x^3 between 0 & 5 with step size of 0.1
    x_start=0
    x_end=5
    step_size=0.1
    
    f1=lambda x:x**3
    area_Y1 = trapezoidal(x_start,x_end,f1)

    f2=lambda x:x**2
    area_Y2 = trapezoidal(x_start,x_end,f2)
    pass
