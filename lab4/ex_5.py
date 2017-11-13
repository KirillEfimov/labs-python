from time import sleep
from librip.ctxmngrs import timer
from librip.gens import gen_random


a=[x for x in gen_random(1,5,1)]
b=[x*x for x in a]
c=list(map(lambda x:x*x, a))
print(a)
print(b)
print(c)

with timer():
    sleep(5.5)
