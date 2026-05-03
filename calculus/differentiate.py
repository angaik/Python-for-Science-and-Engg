def central_differential(f,x,order:int=1):
    """This function returns the differential of a function at a point as per
    central differential method.
    Args:
        f (Callable) : A function.
        x (float) : The point at which differential is calculated.
    Returns:
        The differential.
    """
    step_size = 1e-3
    if order == 1:
        return (f(x+step_size)-f(x-step_size))/(2*step_size)
    elif order == 2:
        return (f(x+step_size)-2*f(x)+f(x-step_size))/pow(step_size,2)
    else:
        ValueError("The function can't compute 3rd+ order differentials.")

if __name__ == "__main__":
    def my_func(x:float)->float:
        return x**2+2*x-4
    
    diff = central_differential(my_func,5,2)
    pass