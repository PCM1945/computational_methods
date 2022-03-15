from file import File


class Point:
    def __init__(self, function, interval, beta_func, precision):
        """
        DESCRIPTION
            class contaning the fixed point method
            the method initial seed is the first value of the interval
        params:
        function(str): function to be analyzed
        interval(tuple [a,b]): interval to be used for the method
        beta_func(str): function(x^n) rewritten as terms of the function cognates
        precision(float): precision to be used for the method
        """
        self.function = function
        self.interval = interval
        self.beta_func = beta_func
        self.precision = float(precision)

    def beta(self, x):
        exec("from math import *")
        # import log module ot work with eval function
        exec("from math import log as ln")
        # translates a  valid expession into python code
        return (eval(self.beta_func))

    def f(self, x):
        exec("from math import *")
        # import log module ot work with eval function
        exec("from math import log as ln")
        # translates a  valid expession into python code
        return float(eval(self.function))

    def fixed_point(self):
        interaction = 0
        x0 = float(self.interval[0])

        f = File(["iter", 'x0', 'f(x)', "b(x)",
                 "|f(x)|", '|xn-xn-1|'], 'fixed.csv')
        f.create_csv()
        data = []
        while True:
            try:
                interaction += 1
                # print(x0)
                x1 = self.beta(x0)
                error1 = abs(self.f(x1))
                error2 = abs(abs(x1 - x0))
                data.extend([interaction, x1, self.f(x0), x1, error1, error2])
                f.write_file(data)
                data.clear()
                if error1 < self.precision or error2 < self.precision:  # compare obtained values with the error
                    # print(x0)
                    print(f"x = {x1}")
                    print(f" interactions = {interaction}")
                    if error1 < error2:
                        print(f" error|f(xn)| = {error1}")
                    else:
                        print(f" error|xn- xn-1| = {error2}")
                    break
                x0 = x1
            except OverflowError:
                print(
                    "fixed point method diverged with given interval (float overflow) \nlast iteration:")
                print(f"Root = {x1}")
                print(f"Interactions = {interaction}")
                break
            except ZeroDivisionError:
                print("zero division error")
                break
