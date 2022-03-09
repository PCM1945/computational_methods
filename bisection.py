from file import File

class Bissection:
    def __init__(self, function, interval, precision):
        """
        DESCRIPTION
            class contaning all bisection methods
        params:
        function(str): function to be analyzed
        interval(tuple[a,b]): interval to be used for the method
        precision(float): precision to be used for the method
        """
        self.function = function
        self.interval = interval
        self.precision = float(precision)

    def fx(self, x):
        exec("from math import *")
        exec("from math import log as ln") # import log module ot work with eval function
        return float(eval(self.function)) # translates a  valid expession into python code

    def bisect(self):
        f = File(['interections','Xa', 'f(xa)', 'Xb', 'f(xb)', 'xn', 'f(xn)', '|fxn|', '|xn- xn-1|'], 'bisection.csv')
        f.create_csv()
        file_data = []

        ia = float(self.interval[0])
        ib = float(self.interval[1])
        if abs(ia - ib) < self.precision: #interval ib is smaller than precision -> root = (a+b)/2
            print("root:", (ia+ib)/2)
            print("interections: 1")
        else:
            interections = 0
            while True:
                try:
                    interections += 1
                    x=(ia + ib)/2 #x as the cetralpoint in [a,b]
                    fx_a= self.fx(ia)#f(a)
                    fx_b= self.fx(ib)#f(b) 
                    f_x=  self.fx(x) #f(x)
                    file_data.extend([interections, ia, fx_a, ib, fx_b, x, f_x,abs(f_x), abs(ib-ia)])
                    f.write_file(file_data)
                    file_data.clear()

                    if abs(f_x) <  self.precision:#se f(x) < precision root = x
                        print(f"Root: {x}")
                        print(f"Interections = {interections + 1}")
                        print(f"error |fx(xn)|: {abs(f_x)}")
                        break
                    if abs(ib - ia) < self.precision: # interval[a,b] < precision -> root = (a+b)/2
                        x = (ia + ib) / 2
                        print(f"Root: {x}")
                        print(f"Interections = {interections + 1}")
                        print(f"error |xn-xn-1|: {abs(ib-ia)}")
                        break
                    elif fx_a * f_x < 0: # f(a) * f(x) < 0-> b = x 
                        ib = x
                    elif fx_a * f_x > 0: # f(a) * f_x > 0 -> a = x
                        ia = x
                except OverflowError:
                    print("bisection method diverged with given interval (float overflow) \nlast iteration:")
                    print(f"Root = {x}")
                    print(f"Interactions = {interections + 1}")
                    break
                except ZeroDivisionError:
                    print("zero division error")
                    break
                