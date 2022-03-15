from sympy import diff, Symbol, lambdify 

def dx(func, x):
       # simb = Symbol('x')
        exec("from math import *")
        exec("from math import log as ln")
        # import log module to work with eval function
        # translates a valid expession into python code
        return float(eval(str(diff(func))))

print(dx('ln(pow(x,2)+ 1)', 2))