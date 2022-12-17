# -*-coding:cp1251-*-
import sys
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
        al = {}
        for i in x:
            al[i] = 0
        fl = len(x)
        for i in x:
            al[i] += 1
        cl=al.copy()
        l = len(al)
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
        for i in bl:
            # bl[i]=(8-len(str(i)))*'0'+bl[i]
            # print(int(bl[i],2))
            bl[i]=chr(int(bl[i],2))


        # непосредственно шифруем
        for i in bl:
            x = x.replace(i, bl[i])

        output = open(out_file, 'w')
        output.write(chr(l) + '\n')
        output.write(str(cl) + '\n')
        output.write(x)
        output.close()
    # дешифруем
    if itype == "--decode":
        input_file = open(input_file)
        holder = ''
        ll = []
        for i in input_file:
            holder += str(i)

        ll = holder.split('\n')



        l = ord(ll[0])

        print(l)

        al = ll[1]
        code = ll[2]



        jo = {}
        ja = {}
        # print(al)

        for i in range(l):
            # jo[al.split(',')[i].split(':')[0].split("'")[1]]=al.split(',')[i].split(':')[1].split("'")[1]
            if "}" in al.split(', ')[i].split(': ')[1]:
                ja[al.split(', ')[i].split(': ')[1][:-1:]] = al.split(', ')[i].split(': ')[0].split("'")[1]
            else:
                ja[al.split(', ')[i].split(': ')[1]] = al.split(', ')[i].split(': ')[0].split("'")[1]



        al=ja.copy()

        bl = al.copy()

        print(ja)
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

        # print(al)
        # print('----------')
        print(bl)

        out = ''

        newlist = []
        notnewlist = []

        for k in ja:
            # в первый список добавляем ключи строками, с целью дальнейшего сравнения подстроки текста с имеющимеся элементами, во второй список добавляем эти же элементы чно цифрами, для поиска наибольшего из них
            try:
                newlist.append(k)
                notnewlist.append(int(k))
            # если мы не можем добавить элемент К, его не существует, тогда длина = 0
            except:
                ma = 0
        try:
            ma = len(str(max(notnewlist)))
        except:
            pass
        # прибавляем к шифрованному тексту столько пробелов, какова максимальная длина ключа шифрованный буквы
        code += ' ' * ma
        i = 0
        # пока остаолсь неравскодированное
        while ('1' in code or '0' in code) and i < len(code) - ma:
            if code[i] == '1' or code[i] == '0':
                ho = ''
                # для элемента i в шифрованному тексте пытаемся найти его в списке ключей, если такого нет то добавляем элемент i+n до тех пор, пока не найдется
                for j in range(ma):
                    ho += str(code[i + j])
                    if ho in newlist:
                        if ja[ho] == "\\n":
                            code = code.replace(ho, '\n', 1)
                        else:
                            code = code.replace(ho, ja[ho], 1)
                            break
            i += 1
        # пишем изменения
        out = code[:-ma]
        out_file = open(out_file, 'w')
        out_file.write(out)
        out_file.close()
# так принято в питоне, если мы станем использовать шифратор в другой программе, это очень удобно
if __name__=='__main__':
    main()