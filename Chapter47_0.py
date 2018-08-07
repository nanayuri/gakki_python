class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

    def __setitem__(self, key, value):
        self.count[key] += 1
        self.values[key] = value
        return self.values[key]

    def __delitem__(self, key):
        self.count[key] -= 1
        del self.values[key]
        self.count.pop(key)
        for each_key in self.count:
            if each_key > key:
                key_val = self.count[each_key]
                self.count.pop(each_key)
                each_key -= 1
                self.count[each_key] = key_val

    def counter(self, index):
        return self.count[index]

    def append(self, value: object) -> object:
        a = len(self.values)
        self.values.append(value)
        self.count[a] = 0

    def pop(self, key):
        self.count[key] -= 1
        del self.values[key]
        a = self.count.pop(key)
        for each_key in self.count:
            if each_key > key:
                key_val = self.count[each_key]
                self.count.pop(each_key)
                each_key -= 1
                self.count[each_key] = key_val
        return a


class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value: object) -> object:
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()




