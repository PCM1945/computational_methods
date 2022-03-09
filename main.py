import re
from bisection import Bissection
from fixed_point import Point 
from newton import Newton
from false_point import Sec 

def capture_basic_data():
    """ 
    Description:
        capture basic data(function, interval, precision).
    params:
        None
    Retruns:
        tuple[function, interval, precision]
    """
    while True:
        try:
            print("Enter the function you wish to analyze use(ln(x), pow(x, n),sqrt(x), e): ")
            function = input()
            interval = []
            a, b = map(float, input("Enter interval (format: 'a b'): ").split())
            interval.append(a)
            interval.append(b)
            precision = input("Enter precision: ")
            return function, interval, precision
        except Exception or KeyboardInterrupt:
            print(" wrong format, try again !!!")

         

def fixed_data():
    """
    Description:
    
        Captures specific fixed point method variables
    """
    print("For the bisection method enter:")
    return input( "The beta function: ")
def newton_data():
    """
    Description:
        Captures specific newton method variables
    """
    print("For the newton method enter:")
    return input("The derivate function f'(x): ")

methods = """
1- Newton-Rphson
2- Fixed point
3- Bissection
4- False point
"""
def main():
    print("ctrl+c to exit")
    while True:
        try:
            print("################################# MAIN MENU #################################")
            print("select what method you would like to process: ", end = '')

            print(methods)

            match input(): 
                case('1'):
                    func,interval, prec = capture_basic_data()
                    dev_x = newton_data()
                    newton = Newton(func,interval, dev_x ,prec)
                    print("Newton: ")
                    newton.newton() 
                case('2'):
                    func,interval, prec = capture_basic_data()
                    beta = fixed_data()
                    fixed= Point(func, interval, beta, prec)
                    print("fixed point: ")    
                    fixed.fixed_point()
                case('3'):
                    func,interval, prec = capture_basic_data()
                    print("bisection: ")
                    bi = Bissection(func, interval, prec)
                    bi.bisect()
                case('4'): 
                    func,interval, prec = capture_basic_data()
                    f_point = Sec(func, interval, prec)
                    f_point.point()
                case _:
                    print("this option does not exists")
            print()
            print("Press Ctrl+C to exit, else try other function")
        except KeyboardInterrupt:
            print("program terminated!!")
            break

if __name__ == "__main__":
    main()
