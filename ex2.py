import re
import sys
from collections import Counter


__search__ = re.compile(r'^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.)' +
                        r'{3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)')
with open('{i}'.format(i=sys.argv[1]), 'r') as file:
    __logs__ = [row.strip() for row in file]


def show_usage():
    print("Нужен аргумент\nНапример: {i} 'name_of.log'".format(i=sys.argv[0]))
    sys.exit(1)


def counter_dict(list_, count=1):
    return Counter(dict([(i, list_.count(i))
                   for i in set(list_)])).most_common(count)


def top5():
    listResult = []
    for i in __logs__:
        listResult.append(''.join(__search__.findall(i)))
    top5 = counter_dict(listResult, 5)
    for i in top5:
        print(i)


def error404():
    listResult = []
    for i in __logs__:
        if __search__.findall(i) and i.find('404') != -1:
            listResult.append(''.join(__search__.findall(i)))
    print(counter_dict(listResult))


def active_time():
    searchtime = re.compile(r'\d{2}:\d{2}:\d{2} ')
    listResult = []
    for i in __logs__:
        listResult.append(''.join(searchtime.findall(i))[0:2])
    print(counter_dict(listResult))


if len(sys.argv) != 2:
    show_usage()
choose = input('Введите пункт меню\n' +
               '1 - TOP-5 (по количеству запросов) IP-адресов\n' +
               '2 - IP-адрес, который больше всех получил 404 статус код' +
               '\n3 - Cамый активный час (по количеству запросов)\n>> ')
if choose == '1':
    top5()
elif choose == '2':
    error404()
elif choose == '3':
    active_time()
else:
    print('Неверный ввод')
    sys.exit(1)
