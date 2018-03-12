import time


class LeapYear:
    def __init__(self):
        self.this_year = time.strftime("%G")
        # print(self.this_year)
        self.year = (i for i in range(int(self.this_year)))
        self.a = filter(lambda x: x % 4 == 0 and x % 100 != 0 or x % 400 == 0, self.year)

    def __iter__(self):
        return self.a

    def __next__(self):
        return next(self.a)


leapYears = LeapYear()

for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        continue