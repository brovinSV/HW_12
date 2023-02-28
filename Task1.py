"""
Створіть функцию, яка обчислює факторіал числа. Запустіть декілька задач,
що використовуватимуть ThreadPoolExecutor. Виміряти швидкість обчислень.
Зробіть теж саме, використовуючи ProcessPoolExecutor. Додайте у програму
код, який порівнює швидкість обчислень і виводить на друк найоптимальніший метод.
"""
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

val = [20, 35, 47, 52, 79]
def fac(n):
    if (n == 1 or n ==0):
        return 1
    else:
        return n * fac(n - 1)


def thread_pool_exe():
    with ThreadPoolExecutor(max_workers=5) as exe:
        exe.submit(fac, val)
        value = exe.map(fac, val)
        for res in value:
            print(res)

def process_pool_exe():
    with ProcessPoolExecutor(max_workers=5) as exe:
        exe.submit(fac, val)
        value = exe.map(fac, val)
        for res in value:
            print(res)

if __name__ == '__main__':
    cur_time1 = time.time()
    thread_pool_exe()
    print(f"Duration time ThreadPoolExecutor: {time.time() - cur_time1}")
    cur_time2 = time.time()
    process_pool_exe()
    print(f"Duration time ProcessPoolExecutor: {time.time() - cur_time2}")
    if (time.time() - cur_time1) < (time.time() - cur_time2):
        print('Best metod: ProcessPoolExecutor')
    elif  (time.time() - cur_time1) > (time.time() - cur_time2):
        print('Best metod: ThreadPoolExecutor')
    else:
        print('Same result')



