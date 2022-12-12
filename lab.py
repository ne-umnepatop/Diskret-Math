# -*-coding:cp1251-*-
import sys
parlist = []
for p in sys.argv:
    parlist.append(p)
itype = parlist[1]
input_file = parlist[2]
out_file = parlist[3]
if itype == "--encode":
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
    l = len(al)
    bl = al.copy()
    for i in bl:
        bl[i] = ''
    if len(al) == 1:
        bl[i] = '0'
    while len(al) > 1:
        a = min(al, key=al.get)
        an = al[a]
        al.pop(a)
        b = min(al, key=al.get)
        bn = al[b]
        al.pop(b)
        for i in a:
            bl[i] = '0' + bl[i]
        for i in b:
            bl[i] = '1' + bl[i]
        al[a + b] = an + bn
    for i in bl:
        x = x.replace(i, bl[i])
    output = open(out_file, 'w')
    output.write(str(l) + '\n')
    output.write(str(bl) + '\n')
    output.write(x + '\n')
    output.close()
if itype == "--decode":
    input_file = open(input_file)
    holder = ''
    ll = []
    for i in input_file:
        holder += str(i)
    ll = holder.split('\n')
    l = int(ll[0])
    al = ll[1]
    code = ll[2]
    jo = {}
    ja = {}
    for i in range(l):
        ja[al.split(', ')[i].split(': ')[1].split("'")[1]] = al.split(', ')[i].split(': ')[0].split("'")[1]
    out = ''
    newlist = []
    notnewlist = []
    for k in ja:
        try:
            newlist.append(k)
            notnewlist.append(int(k))
        except:
            ma = 0
    try:
        ma = len(str(max(notnewlist)))
    except:
        pass
    code += ' ' * ma
    i = 0
    while ('1' in code or '0' in code) and i < len(code) - ma:
        if code[i] == '1' or code[i] == '0':
            ho = ''
            for j in range(ma):
                ho += str(code[i + j])
                if ho in newlist:
                    if ja[ho] == "\\n":
                        code = code.replace(ho, '\n', 1)
                    else:
                        code = code.replace(ho, ja[ho], 1)
                        break
        i += 1
    out = code[:-ma]
    out_file = open(out_file, 'w')
    out_file.write(out)
    out_file.close()
