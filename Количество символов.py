from collections import Counter
def cnt(f):
    '''Функция возвращает словарь из пар буква:количество букв.
    На вход подаётся txt файл, например, так:
    with open('disk.txt.txt') as f:
        print(cnt(f))'''
    a = []
    for str in f.readlines():
        a+=Counter(str).most_common()
    letter = []
    amount = []
    for x, y in a:
        if letter.count(x) < 1:
            letter.append(x)
            amount.append(y)
        else:
            amount[letter.index(x)] += y
    c=sorted(amount)
    ltrs=[]
    for i in range(len(c)):
        ltrs.append(letter[amount.index(c[i])])
        letter.pop(amount.index(c[i]))
        amount.pop(amount.index(c[i]))
    a = dict(zip(ltrs, c))
    return a


txt='input_file.txt'
with open(f'{txt}') as f:
    print(cnt(f))



