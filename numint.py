
def midpt(x_start,x_end,f):
    I_midpt=(x_end-x_start)*f((x_start+x_end)/2)
    return I_midpt

def comp_midpt(x_start,x_end,step_size,Y):
    I_comp_midpt=step_size*sum(Y)
    # Experiment with not adding return statement

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