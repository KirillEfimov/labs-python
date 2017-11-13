import sys
import json
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

try:
    path = "data_light.json"
except IndexError:
    raise ValueError('Path to data file is not specified')

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


@print_result
def f1(arg):
    return sorted(unique(field(arg,'job-name'),ignore_case=True),key=lambda x: x.lower())
#    raise NotImplemented


@print_result
def f2(arg):
    print()
    return list(filter(lambda x:x.lower().startswith('программист'),arg))
#    raise NotImplemented


@print_result
def f3(arg):
    print()
    return list(map(lambda x: x+" с опытом Python",arg))
#    raise NotImplemented


@print_result
def f4(arg):
    print()
    rand = gen_random(100000,200000,len(arg))
    return list(map(lambda s:s[0]+', с зарплатой '+str(s[1]),zip(arg,rand)))
#    raise NotImplemented
    

with timer():
    f4(f3(f2(f1(data))))
