import calculus.integrate as integrate

def compound_interest(years):
    return 100*pow(1+0.12,years)

x = integrate.comp_midpt(1,4,compound_interest)
pass