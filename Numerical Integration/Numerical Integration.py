# Numerical Integration
import numpy as np

# Numerical Integration of f(x) = x^4 + 8*x^3 - 5*x^2 + 9*x - 41 between 0 & 5 with step size of 0.1
f=lambda x:x**2
x_start=0
x_end=5
step_size=0.1
X=np.arange(x_start,x_end+step_size,step_size)
Y=f(X)

# Integration by midpoint rule
# I = (x_end-x_start)*f(x_avg)
I_midpt=(x_end-x_start)*f((x_start+x_end)/2)
print(f"The integral by midpoint method is {I_midpt}.")

# Integration by composite mid-point rule
# I = step_size*sum(f(x_i))
I_comp_midpt=step_size*sum(Y)
print(f"The integral by composite midpoint method is {I_comp_midpt}.")

# Integration by trapezoidal method
I_trapezoidal=(x_end-x_start)*((f(x_start)+f(x_end))/2)
print(f"The integral by trapezoidal method is {I_trapezoidal}.")

# Integration by composite trapezoidal rule
S_intermediate=sum(Y)-Y[0]-Y[-1]
I_comp_trapezoidal=((x_end-x_start)/(2*len(X)))*(Y[0]+Y[-1]+2*S_intermediate)
print(f"The integral by composite trapezoidal rule is {I_comp_trapezoidal}.")

# Simpson's 1/3rd rule
I_Simp_13=(step_size/3)*(Y[0]+Y[-1]+4*S_intermediate)
print(f"The integral by Simpson's 1/3rd rule is {I_Simp_13}.")

# Composite Simpson's 1/3rd rule
Y_even=[Y[i] for i in range(1,len(Y)-1) if i%2==0]
S_even=sum(Y_even)
Y_odd=[Y[i] for i in range(1,len(Y)-1) if i%2==1]
S_odd=sum(Y_odd)
I_comp_Simp_13=(step_size/3)*(Y[0]+Y[-1]+4*S_odd+2*S_even)
print(f"The integral by composite Simpson's 1/3rd rule is {I_comp_Simp_13}.")

print(f"For comparison, the exact integral value is {125/3}")
