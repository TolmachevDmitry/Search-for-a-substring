from boyer_moor_algorithm import bm
from get_symbols import symbols
import matplotlib.pyplot as plt
from time import time
from brute_force import b_force as bf
import random


def get_text(sy, le):
    ans = ""
    for _ in range(0, le):
        ans += sy[random.randint(0, len(sy) - 1)]
    return ans


def get_estimate(co, sy, f):
    time_list = list()

    for n in co:
        y = get_text(sy, n)
        times = list()
        x = y[len(y) - 8: len(y)]

        for _ in range(10):
            t = time()
            f(y, x)
            times.append((time() - t) * 1000000)

        time_list.append(sum(times) / len(times))

    return time_list


sym = symbols()

n_count = 30

count = [i for i in range(1000, n_count * 1000 + 1, 1000)]

time_list1, time_list2 = get_estimate(count, sym, bf), get_estimate(count, sym, bm)

time_list1, time_list2, count = [i / 1000 for i in time_list1], [i / 1000 for i in time_list2], [i / 1000 for i in count]


middle = int(n_count / 2)

plt.plot(count, time_list1, label="Brute force")
plt.plot(count, time_list2, label="Boyer-Moor")
plt.title("Замеры времени выполнения алгоритмов \"Brute force\" и Бойера-Мура")
plt.ylabel("Время (тыс. м/с)")
plt.xlabel("Количество символов (тыс.)")

plt.grid(True)
plt.legend()
plt.show()
