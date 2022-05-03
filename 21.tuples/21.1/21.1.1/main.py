import random

list1 = (random.randint(0, 5) for _ in range(10))
list2 = (random.randint(-5, 0) for _ in range(10))

tuple1 = tuple(list1)
tuple2 = tuple(list2)

tuple3 = tuple1 + tuple2
count_zero = tuple3.count(0)
print('объединенный кортеж:', tuple3, 'кол-во нулей:', count_zero)