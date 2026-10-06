import calculus.integrate as integrate

def test_func(a:float)->float:
    return a**3 + 2*a**2 - 3*a + 4

x = integrate.comp_simpson_13(1,4,0.1,test_func)
y = integrate.comp_trapezoidal(1,4,0.1,test_func)
pass