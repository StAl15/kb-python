import time

'''
Копейцев обязательно спросит что такое кеширующий декоратор :)))))
Написать его несложно, его суть кешировать значения функции и в нужный момент доставать их по ключу. 
Ключ например мы можем сгенерировать из аргументов
'''

def decorator(func):
    """Кэш предыдущих вызовов функций"""
    cache = {}
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]
    return wrapper


#пример для подсчета чисел фибоначи
@decorator
def fib1(num):
    if num < 2:
        return num
    return fib1(num - 1) + fib1(num - 2)

def fib2(num):
    if num < 2:
        return num
    return fib2(num - 1) + fib2(num - 2)

'''
Чтоб понять какой импакт от этой херни, посмотрим разницу во времени
'''

start1 = time.perf_counter(); fib1(100); print('Time cached fib with 100 run:', time.perf_counter() - start1)
start2 = time.perf_counter(); fib2(30); print('Time not cached fib with 30 run:', time.perf_counter() - start2)