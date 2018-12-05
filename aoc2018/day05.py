from util import load_data, readlines_, timer
from string import ascii_lowercase
from functools import reduce

def process(s):
    def _react(x, xs):
        if x and xs and abs(ord(x[-1]) - ord(xs[0])) == 32:
            return x[:-1]
        else:
            return x + xs[0]

    return len(reduce(_react, s))


@timer
def part1(data):
    return process(data)


@timer
def part2(data):
    return min(process(data.replace(c, '').replace(c.upper(), ''))
               for c in ascii_lowercase)


def main():
    with load_data(day=5) as fp:
        data = tuple(readlines_(fp))[0]

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
