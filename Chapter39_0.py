class Calc:
    count = 0

    def __init__(self):
        Calc.count += 1

    def __del__(self):
        Calc.count -= 1
