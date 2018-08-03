import bisect
import Levenshtein

def closest(haystack, needle):
    if len(haystack) == 0:
        return None, None
    index = bisect.bisect_left(haystack, needle)
    if index == 0:
        return None, haystack[0]
    if index == len(haystack):
        return haystack[index], None
    if haystack[index] == needle:
        return haystack[index], haystack[index]
    return haystack[index-1], haystack[index]

list1 = ['v0_label(0)\n值0标签','v1_label(1)\n值1标签','v2_label(10)\n值2标签','v3_label(11)\n值3标签','v4_label(100)\n值4标签','v5_label(101)\n值5标签','v6_label(110)\n值6标签','v7_label(111)\n值7标签','ReturnCond_TO\n反馈控制超时时间']
list1 = [list1[x].upper() for x in range(0, len(list1))]
s1 = 'RETURN'
list2 = [Levenshtein.ratio(s1, str(each)) for each in list1]
dict1 = {list2[x]: list1[x] for x in range(len(list1))
print(dict1)


def find_closest(word, list1):
    list3 = [list1[x].upper() for x in range(0, len(list1))]
    list2 = [Levenshtein.ratio(word.upper(), str(each)) for each in list3]
    dict1 = {list2[x]: list1[x] for x in range(len(list1))}
    return dict1[max(dict1)]


def get_col_num():

