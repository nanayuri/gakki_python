class Counter:
    def __init__(self):
        self.counter = 0

    def __setattr__(self, name, value):
        if name == 'counter':
            super().__setattr__(name, value)
        else:
            self.counter += 1
            super().__setattr__(name, value)

    def __delattr__(self, name):
        self.counter -= 1
        super().__delattr__(name)
