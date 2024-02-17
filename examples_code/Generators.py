# Написать генераторную функцию, которая возвращает все перестановки дан vuного списка. (без itertools.permutations)
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]  # смещаем каждый раз первый элемент вперед и записываем


arr = [1, 2, 3, 4, 5]
rs = list(all_perms(arr))
print(rs)
