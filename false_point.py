from file import File
class Sec:
    """DESCRIPTION
            class contaning newton-Raphson method
            the method initial seed is the first value of the interval
        params:
        function(str): function to be analyzed
        interval(tuple [a,b]): interval to be used for the method
        precision(float): precision to be used for the method
    """
    def __init__(self, function, interval, precision):
        self.function = function
        self.interval = interval
        self.precision = float(precision)
    
    def f(self, x):
        exec("from math import *")
        exec("from math import log as ln") # import log module ot work with eval function
        return float(eval(self.function)) # translates a valid expession into python code

    def point(self):
        i = 0
        f = File([ 'iter','xa', 'f(xa)', 'xb', 'f(xb)', '|xn-xn-1|', '|f(x)|', '|f(xa)|', '|f(xa)|'], 'false.csv')
        f.create_csv()
        data = []
        a = self.interval[0]
        b = self.interval[1]
        while True:
            try:
                i += 1 
                fxa = self.f(a)
                fxb = self.f(b)

                ez = ((a * fxb) - (b * fxa)) / (fxb - fxa) #calculates approximated zero
                fx = self.f(ez)

                data.extend([i, a, fxa, b, fxb, abs(b - a), abs(fxa), abs(fxb), abs(fx)])
                f.write_file(data)
                data.clear()    
                
                if abs(b - a) < self.precision: # the root is the medium point of [a,b]
                    ez = ((b + a) / 2)
                    print(f"error |b-a|: {abs(b - a)}")
                    print(f"Root = {ez}")
                    print(f"Interactions = {i}")
                    break
                if abs(fxa) < self.precision:
                    ez = a
                    print(f'error |f(Xa)|: {fxa}')
                    print(f"Root = {ez}")
                    print(f"Interactions = {i}")
                    break
                if abs(fxb) < self.precision:
                    ez = b
                    print(f"Root = {ez}")
                    print(f"Interactions = {i}")
                    print(f'error |f(xb)|: {abs(fxb)}')
                    break
                if abs(fx) < self.precision:
                    print(f"Root = {ez}")
                    print(f"Interactions = {i}")
                    print(f"error |f(x)|: {abs(fx)}")
                    break

                if fxa * fx < 0: # check if value between [a,b]
                    b = ez
                elif fxa * fx > 0: # check if value between [a,b]
                    a = ez

            except OverflowError:
                print("false point method diverged with given interval (float overflow) \nlast iteration:")
                print(f"Root = {ez}")
                print(f"Interactions = {i + 1}")
                break
            except ZeroDivisionError:
                print("zero division error")
                break