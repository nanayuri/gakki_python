'''
有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；

要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小

'''

import random
import time
import functools


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


class Min_Value:
    def __init__(self):
        self.n = random.randint(1, 1000)
        self.a = []
        self.b = []
        for i in range(1, self.n):
            self.a.append(random.randint(1, 1000))
            self.b.append(random.randint(1, 2000))

    @functools.lru_cache()
    @clock
    def minival(self):
        a = self.a
        b = self.b
        total = abs(sum(a) - sum(b))
        a_org = a.copy()
        b_org = b.copy()
        i = 0
        while i < len(a):
            each_a = a[i]
            exg_val = 0
            j = 0
            while j < len(b):
                each_b = b_org[j]
                total_new = abs(sum(a_org) - each_a + each_b - (sum(b_org) + each_a - each_b))
                if total_new < total:
                    total = total_new
                    exg_val = each_b
                j += 1
            # print(total, exg_val)
            # print(a)
            # print(b)
            # print(a_org)
            # print(b_org)
            if exg_val != 0:
                print(each_a, exg_val, total)
                a_org.remove(each_a)
                a_org.append(exg_val)
                b_org.remove(exg_val)
                b_org.append(each_a)
            i += 1
        return total, a_org, b_org


if __name__ == '__main__':
    diff_value = Min_Value()
    list_a = []
    list_b = []
    total, list_a, list_b = diff_value.minival()
    print("每个序列中各有%i个元素" % diff_value.n)
    print("调换元素顺序后，两序列的差的最小值为: ", total)
    print("调换前第一个序列为：\n", diff_value.a)
    print("调换前第二个序列为：\n", diff_value.b)
    print("调换后第一个序列为：\n", list_a)
    print("调换后第二个序列为：\n", list_b)
