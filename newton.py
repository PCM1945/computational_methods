from file import File
class Newton:
    def __init__(self, function, interval, derivative_func, precision):
        """
        DESCRIPTION
            class contaning newton-Raphson method
            the method initial seed is the first value of the interval
        params:
        function(str): function to be analyzed
        interval(tuple [a,b]): interval to be used for the method
        derivative_func(str):  first derivative of the function to be used for the method
        precision(float): precision to be used for the method
        """
        self.function = function
        self.interval = interval
        self.derivative_func = derivative_func
        self.precision = float(precision)

    def dx(self, x):
        exec("from math import *")
        exec("from math import log as ln") # import log module to work with eval function
        return float(eval(self.derivative_func)) # translates a valid expession into python code

    def fx(self, x):
        exec("from math import *")
        exec("from math import log as ln")# import log module to work with eval function
        return float(eval(self.function)) # translates a valid expession into python code

    def newton(self):
        i = 0
        x0 = self.interval[0]
        f = File(["iter",'x0', 'f(x)', "f'(x)", "|f(x)|", '|xn-xn-1|'], 'newton.csv')
        f.create_csv()
        data = []
        while True:
            try: 
                i += 1
                x = x0 - self.fx(x0) / self.dx(x0)
                error1  = abs(self.fx(x))
                error2 = abs(x-x0)

                data.extend([i, x, self.fx(x0), self.dx(x0), error1, error2])
                f.write_file(data)
                data.clear()

                if error1 < self.precision or  error2 < self.precision: # compare obtained values with the error
                    print(f"Root = {x}")
                    print(f"Interactions = {i}")
                    if error1 < error2:
                        print(f'error |f(x)|: {error1}')
                    else:
                        print(f'error |xn-xn-1|: {error2}')
                    break
                else:
                    x0=x
               
            except OverflowError:
                print(f"Newton method diverged with given X0 {self.interval[0]} (float overflow) \nlast iteration:")
                print(f"Root = {x}")
                print(f"Interactions = {i + 1}")
                break
            except ZeroDivisionError:
                print("zero division error")
                break
