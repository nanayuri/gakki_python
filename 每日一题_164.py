
vowel_num = []
vowel_list = ['a', 'e', 'i', 'o', 'u']


def swap_vowel(word):
    num = 0
    for each_word in word:
        if each_word in vowel_list:
            vowel_num.append(each_word)
            num += 1
    vowel1 = vowel_num[0]
    vowel2 = vowel_num[1]
    #print(vowel1, vowel2)
    if num != 2 or (num == 2 and vowel1 == vowel2):
        return None
    else:
        str1 = str(word).replace(vowel1, '$').replace(vowel2, vowel1).replace('$', vowel2)
        #str1 = str1.replace(vowel2, vowel1)
        #str1 = str1.replace('$', vowel2)
        return str1

a = swap_vowel('apple')
print(a)