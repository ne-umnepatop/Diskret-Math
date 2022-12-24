# -*-coding:cp1251-*-
import sys

def kod(al):
    global bl
    # получаем словарь из пар символ - пустой символ
    bl = al.copy()
    for i in bl:
        bl[i] = ''
    # если во всём тексте только один символ, кодируем его 0
    if len(al) == 1:
        bl[i] = '0'
    # пока остались незакодированные символы
    while len(al) > 1:
        # а - индекс самого редкого символа
        a = min(al, key=al.get)
        # an - самый редкий символ
        an = al[a]
        # убираем из al
        al.pop(a)
        # то же с б
        b = min(al, key=al.get)
        bn = al[b]
        al.pop(b)
        # таким образом происходит создание шифра, для одного элемента приписывается ноль, для другого еденица
        for i in a:
            bl[i] = '0' + bl[i]
        for i in b:
            bl[i] = '1' + bl[i]
        # объединили два символа с наименьшей  частотностью встреч
        al[a + b] = an + bn
        print(bl)
        return bl
def main():
    # работа с опциями из командной строки
    parlist = []
    for p in sys.argv:
        parlist.append(p)
    itype = parlist[1]
    input_file = parlist[2]
    out_file = parlist[3]
    # шифровка
    if itype == "--encode":
        # составление словаря из пар символ - частота встреч
        f = open(input_file)
        x = ''
        for i in f:
            x += i
        x = x.replace('\n', '`')
        al = {}
        for i in x:
            al[i] = 0
        fl = len(x)
        for i in x:
            al[i] += 1
        cl = ''
        for i in al:
            cl += i + ':'
            cl += chr(al[i]) + ':'
        cl = cl[:-1]
        # получаем словарь из пар символ - пустой символ
        bl = al.copy()
        for i in bl:
            bl[i] = ''
        # если во всём тексте только один символ, кодируем его 0
        if len(al) == 1:
            bl[i] = '0'
        # пока остались незакодированные символы
        while len(al) > 1:
            # а - индекс самого редкого символа
            a = min(al, key=al.get)
            # an - самый редкий символ
            an = al[a]
            # убираем из al
            al.pop(a)
            # то же с б
            b = min(al, key=al.get)
            bn = al[b]
            al.pop(b)
            # таким образом происходит создание шифра, для одного элемента приписывается ноль, для другого еденица
            for i in a:
                bl[i] = '0' + bl[i]
            for i in b:
                bl[i] = '1' + bl[i]
            # объединили два символа с наименьшей  частотностью встреч
            al[a + b] = an + bn
        # bl=kod(al)
        # непосредственно шифруем
        for i in bl:
            x = x.replace(i, bl[i])
        if len(x) % 8 != 0:
            x = (8 - len(x) % 8) * '0' + x
        y = ''
        for i in range(0, len(x), 8):
            if chr(int(x[i:i + 8], 2)) == '\n':
                y += ''
            else:
                y += chr(int(x[i:i + 8], 2))
        output = open(out_file, 'w', encoding="utf-8")
        output.write(chr(len(bl)) + '\n')
        output.write(str(cl) + '\n')
        output.write(y)
        output.close()
    # дешифруем
    if itype == "--decode":
        input_file = open(input_file, encoding="utf-8")
        holder = ''
        ll = []
        for i in input_file:
            holder += str(i)
        ll = holder.split('\n')
        l = ord(holder[0])
        holder = holder.replace(holder[0], '', 1)
        holder = holder.replace('\n', '', 1)
        tagir = []
        for i in range(0, l * 4, 4):
            tagir.append(holder[i])
            tagir.append(ord(holder[i + 2]))
        for i in range(len(tagir)):
            if tagir[i] == 10:
                tagir[i] = 13
        holder = holder[l * 4:]
        cle = tagir[0]
        slov = {}
        for i in range(0, len(tagir) - 1, 2):
            try:
                slov[tagir[i]] = int(tagir[i + 1])
            except:
                pass
        code = holder
        al = slov.copy()
        bl = al.copy()
        for i in bl:
            bl[i] = ''
        # если во всём тексте только один символ, кодируем его 0
        if len(al) == 1:
            bl[i] = '0'
        # пока остались незакодированные символы
        while len(al) > 1:
            # а - индекс самого редкого символа
            a = min(al, key=al.get)
            # an - самый редкий символ
            an = al[a]
            # убираем из al
            al.pop(a)
            # то же с б
            b = min(al, key=al.get)
            bn = al[b]
            al.pop(b)
            # таким образом происходит создание шифра, для одного элемента приписывается ноль, для другого еденица
            for i in a:
                bl[i] = '0' + bl[i]
            for i in b:
                bl[i] = '1' + bl[i]
            # объединили два символа с наименьшей частотностью встреч
            al[a + b] = an + bn
        cl = {}
        for i in bl:
            cl[bl[i]] = i
        unarchived = ''
        for i in code:
            g = (bin(ord(i))[2:])
            unarchived += (8 - len(g)) * '0' + str(g)
        unarchived = unarchived.replace(bl[cle], cle, 1)
        for i in range(8):
            if unarchived[i] == cle:
                unarchived = unarchived[i:]
                break
        newlist = []
        notnewlist = []
        ma = 0
        for k in cl:
            # в первый список добавляем ключи строками, с целью дальнейшего сравнения подстроки текста с имеющимеся элементами, во второй список добавляем эти же элементы чно цифрами, для поиска наибольшего из них
            try:
                newlist.append(k)
                notnewlist.append(int(k))
            # если мы не можем добавить элемент К, его не существует, тогда длина = 0
            except:
                pass
        try:
            ma = len(str(max(notnewlist)))
        except:
            pass
        # прибавляем к шифрованному тексту столько пробелов, какова максимальная длина ключа шифрованный буквы
        unarchived += ' ' * ma
        i = 0
        # пока остаолсь неравскодированное
        while ('1' in unarchived or '0' in unarchived) and i < len(unarchived) - ma:
            if unarchived[i] == '1' or unarchived[i] == '0':
                ho = ''
                # для элемента i в шифрованному тексте пытаемся найти его в списке ключей, если такого нет то добавляем элемент i+n до тех пор, пока не найдется
                for j in range(ma):
                    ho += str(unarchived[i + j])
                    if ho in newlist:
                        # print(ho)
                        unarchived = unarchived.replace(ho, cl[ho], 1)
            i += 1
        unarchived = unarchived.replace('`', '\n')
        # пишем изменения
        out = unarchived[:-ma]
        out_file = open(out_file, 'w', encoding='utf-8')
        out_file.write(out)
        out_file.close()
# так принято в питоне, если мы станем использовать шифратор в другой программе, это очень удобно
if __name__ == '__main__':
    main()
