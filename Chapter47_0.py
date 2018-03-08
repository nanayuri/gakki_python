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





    def append(self, value):
        self.values.append() self.value
        return self.values


