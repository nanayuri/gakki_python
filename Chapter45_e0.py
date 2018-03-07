class C:
    def __getattr__(self, name):
        print('该属性不存在!')
