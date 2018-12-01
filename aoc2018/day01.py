from util import load_data, readlines_, timer
from itertools import cycle


@timer
def part1(data):
    return sum(map(int, data))


@timer
def part2(data):
    seen = set()
    s = 0
    for i in cycle(map(int, data)):
        if s in seen:
            return s
        else:
            seen.add(s)
        s += i


def main():
    with load_data(day=1, part=1) as fp:
        content = readlines_(fp)

    print(part1(content))   
    print(part2(content))


if __name__ == '__main__':
    main()
