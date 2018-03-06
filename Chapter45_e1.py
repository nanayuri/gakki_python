class Demo:
    def __getattr__(self, name):
        print('FishC')

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
