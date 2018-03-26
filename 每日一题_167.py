list1 = [33,54,29,7555,83,15,318,30,88,1]
list2 = []


def new_lis(*args):
    str1 = ''
    new_list = []
    count_list = []
    for each in args:
        count_list.append(len(str(each)))
        str1 += str(each)
    print(len(str1))
    i = count_list[0] - 1
    c_list = count_list[1:]
    print(i)
    for each in c_list:

        num = int(str1[i : i + each])

        new_list.append(num)
        i += each
        while i >= len(str1):
            break
    new_list.insert(0, int(str1[-1] + str1[0 : 0 + count_list[0] - 1]))
    return new_list

list2 = new_lis(*list1)
print(list2)