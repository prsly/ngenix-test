import re
import sys

from log import Log

__search_re__ = re.compile(r'^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.)' +
                           r'{3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)')


def show_usage():
    print("Нужен аргумент\nНапример: {i} 'name_of.log'".format(i=sys.argv[0]))
    sys.exit(1)


def top5():
    top5 = log.search(__search_re__, 5)
    for i in top5:
        print(i)


def error404():
    print(log.search(__search_re__, code='404'))


def active_time():
    searchtime_re = re.compile(r'\d{2}:\d{2}:\d{2} ')
    print(log.searchtime(searchtime_re))


if len(sys.argv) != 2:
    show_usage()
log = Log(sys.argv[1])
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
