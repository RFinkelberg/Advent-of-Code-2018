from util import load_data, readlines_, timer
from collections import deque
from itertools import compress


def sum_metadata(data):
    n_children = data.popleft()
    n_metadata = data.popleft()

    children = sum(sum_metadata(data) for _ in range(n_children))
    metadata = sum(data.popleft() for _ in range(n_metadata))
    return children + metadata

def sum_values(data):
    n_children = data.popleft()
    n_metadata = data.popleft()

    if n_children == 0:
        return sum(data.popleft() for _ in range(n_metadata))
    else:
        values = [sum_values(data) for _ in range(n_children)]
        metadata = [data.popleft() for _ in range(n_metadata)]

        val = 0
        for idx in metadata:
            idx -= 1
            if idx in range(n_children):
                val += values[idx]
        return val



@timer
def part1(data):
    data = deque(int(i) for i in data.strip('\n').split())
    return sum_metadata(data)


@timer
def part2(data):
    data = deque(int(i) for i in data.strip('\n').split())
    return sum_values(data)


def main():
    with load_data(day=8) as fp:
        data = fp.read()

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
