from util import load_data, readlines_, timer
from functools import partial
from itertools import product
import numpy as np


def power_lvl(x, y, serial, size=3):
    xx, yy = np.meshgrid(np.arange(x, x + size, 1),
                         np.arange(y, y + size, 1))
    lvl = xx + 10
    lvl = lvl * yy
    lvl += serial
    lvl *= xx + 10
    lvl = (lvl // 100) % 10
    lvl = lvl - 5

    return lvl.sum()
    

@timer
def part1(data):
    xs = range(1, 299)
    ys = range(1, 299)
    block = partial(power_lvl, serial=data)
    return max(product(xs, ys), key=lambda p: block(*p))


@timer
def part2(data):
    cell = partial(power_lvl, serial=data, size=1)
    integral = np.zeros((300, 300))

    for i in range(integral.shape[0]):
        for j in range(integral.shape[1]):
            integral[i, j] = (cell(i, j)
                              + integral[i, j - 1]
                              + integral[i - 1, j]
                              - integral[i - 1, j - 1])

    argmax = None
    highest = float('-inf')
    xs = range(1, 299)
    ys = range(1, 299)

    def _total_power(x1, y1, size):
        x2 = x1 + size
        y2 = y1 + size
        # inclusion exclusion
        return integral[x2, y2] - integral[x2, y1] - integral[x1, y2] + integral[x1, y1]

    for x in xs:
        for y in ys:
            sizes = range(1, 300 - max(x, y))
            for size in sizes:
                power = _total_power(x, y, size)
                if power > highest:
                    argmax = (x, y, size)
                    highest = power

    return (argmax[0] + 1, argmax[1] + 1, argmax[2])


def main():
    data = 7315

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
