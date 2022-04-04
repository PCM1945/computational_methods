from bisection import Bissection
from fixed_point import Point
from newton import Newton
from false_point import Sec


def capture_basic_data():
    """Description:
        capture basic data(function, interval, precision).
    params:
        function(str): Math function to be analyzed
        interval(tuple):interval of values to be used
        precision(float): precision to be used as stoping paramiter
    Retruns:
        tuple[function, interval, precision]
    """
    while True:
        try:
            print(
                "Enter the function you wish to analyze use(ln(x), pow(x, n),sqrt(x), e): ")
            function = input()
            interval = []
            a, b = map(
                float, input("Enter interval (format: 'a b'): ").split())
            interval.append(a)
            interval.append(b)
            precision = input("Enter precision: ")
            return function, interval, precision
        except Exception or KeyboardInterrupt:
            print(" wrong format, try again !!!")


def fixed_data():
    """Description:
            Captures specific fixed point method variables
        params:
            None
        returns:
            the beta function "f(x) => x inputted by the user"
    """
    return input("For the bisection method enter:\nThe beta function: ")

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
            print(
                "################################# MAIN MENU #################################")
            print("select what method you would like to process: ", end='')

            print(methods)
            ens = input()
            if ens == '1':
                func, interval, prec = capture_basic_data()
                newton = Newton(func, interval, prec)
                print("Newton: ")
                newton.newton()
                ens = 0
            if ens == '2':
                func, interval, prec = capture_basic_data()
                beta = fixed_data()
                fixed = Point(func, interval, beta, prec)
                print("fixed point: ")
                fixed.fixed_point()
                ens = 0
            if ens == '3':
                func, interval, prec = capture_basic_data()
                print("bisection: ")
                bi = Bissection(func, interval, prec)
                bi.bisect()
                ens = 0
            if ens =='4':
                func, interval, prec = capture_basic_data()
                f_point = Sec(func, interval, prec)
                f_point.point()
                ens = 0
            elif ens != 0:
                print("this option does not exists")
            print()
            print("Press Ctrl+C to exit, else try other function")
        except KeyboardInterrupt:
            print("program terminated!!")
            break


if __name__ == "__main__":
    main()
