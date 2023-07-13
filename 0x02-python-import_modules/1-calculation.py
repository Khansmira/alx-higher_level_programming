#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5
    add = calculator.add(a, b)
    sub = calculator.sub(a, b)
    mul = calculator.mul(a, b)
    div = calculator.div(a, b)
    print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(a, b, add, a, b, sub, a, b, mul, a, b, div))
