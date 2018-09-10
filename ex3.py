# coding: utf-8
import sys


def show_usage():
    print("Нужен аргумент\nНапример: {i} '[][]]['".format(i=sys.argv[0]))
    sys.exit(1)


def balance(brackets):
    stack = []
    for i in brackets:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if ((len(stack) > 0) and ('[' == stack[len(stack)-1])):
                stack.pop()
            else:
                stack = ' '
                break
    if len(stack) == 0:
        return 'Корректно закрыты скобки'
    else:
        return 'Некорректно закрыты скобки'


if len(sys.argv) != 2:
    show_usage()
print(balance(sys.argv[1]))
