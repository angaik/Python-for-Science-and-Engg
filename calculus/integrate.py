"""
This module contains functions to numerically integrate functions over a domain.
"""

def midpt(x_start,x_end,f):
    I_midpt=(x_end-x_start)*f((x_start+x_end)/2)
    return I_midpt

def comp_midpt(x_start,x_end,f):
    """
    Args:
        x_start, x_end (float) : Starting and ending points.
        f (Callable) : A function
    """
    n_points = 10
    step_size = (x_end-x_start)/n_points
    x = [x_start + i*step_size for i in range(n_points)]
    y = [f(point) for point in x]
    return step_size*sum(y)
     

def trapezoidal(x_start,x_end,f):
    I_trapezoidal=(x_end-x_start)*((f(x_start)+f(x_end))/2)
    return I_trapezoidal

def comp_trapezoidal(x_start,x_end,step_size,Y):
    length_x=int((x_end-x_start)/step_size)+1
    S_intermediate=sum(Y)-Y[0]-Y[-1]
    I_comp_trapezoidal=((x_end-x_start)/(2*length_x))*(Y[0]+Y[-1]+2*S_intermediate)
    return I_comp_trapezoidal

def simpson_13(step_size,Y):
    S_intermediate=sum(Y)-Y[0]-Y[-1]
    I_Simp_13=(step_size/3)*(Y[0]+Y[-1]+4*S_intermediate)
    return I_Simp_13

def comp_simpson_13(step_size,Y):
    Y_even=[Y[i] for i in range(1,len(Y)-1) if i%2==0]
    S_even=sum(Y_even)
    Y_odd=[Y[i] for i in range(1,len(Y)-1) if i%2==1]
    S_odd=sum(Y_odd)
    I_comp_Simp_13=(step_size/3)*(Y[0]+Y[-1]+4*S_odd+2*S_even)
    return I_comp_Simp_13

if __name__ == "__main__":
    import numpy as np
    # Numerical Integration of f(x) = x^3 between 0 & 5 with step size of 0.1
    x_start=0
    x_end=5
    step_size=0.1
    X=np.arange(x_start,x_end+step_size,step_size)
    
    f1=lambda x:x**3
    Y1=f1(X)
    area_Y1 = trapezoidal(x_start,x_end,f1)

    f2=lambda x:x**2
    Y2 = f2(X)
    area_Y2 = trapezoidal(x_start,x_end,f2)
    pass
