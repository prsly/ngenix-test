import re
import sys
from collections import Counter


def show_usage():
    print("Нужен аргумент\nНапример: {i} 'name_of.log'".format(i=sys.argv[0]))
    sys.exit(1)


def top5():
    listResult = []
    for i in logs:
        listResult.append(''.join(search.findall(i)))
    top5 = CounterDict(listResult, 5)
    for i in top5:
        print(i)


def error404():
    listResult = []
    for i in logs:
        if search.findall(i) and i.find('404') != -1:
            listResult.append(''.join(search.findall(i)))
    print(CounterDict(listResult))


def CounterDict(list_, count=1):
    return Counter(dict([(i, list_.count(i))
                   for i in set(list_)])).most_common(count)


search = re.compile(r'^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.)' +
                    r'{3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)')
if len(sys.argv) != 2:
    show_usage()
with open('{i}'.format(i=sys.argv[1]), 'r') as file:
    logs = [row.strip() for row in file]
choose = int(input('Введите пункт меню\n' +
                   '1 - TOP-5 (по количеству запросов) IP-адресов\n' +
                   '2 - IP-адрес, который больше всех получил 404 статус код' +
                   '\n3 - Cамый активный час (по количеству запросов)\n>> '))
if choose == 1:
    top5()
elif choose == 2:
    error404()
elif choose == 3:
    activetime()
else:
    print('Неверный ввод')
    sys.exit(1)
