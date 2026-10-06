def explicit_euler(func,initial_value):
    """
    Explicit Euler method for ODE.
    """
    step_size = 1e-2
    return initial_value + step_size * central_differential(func,initial_value)


if __name__ == "__main__":
    from calculus import central_differential
    def my_func(x:float)->float:
        return x**2 + x

    initial_x = 2
    next_x = explicit_euler(my_func,initial_x)

    pass