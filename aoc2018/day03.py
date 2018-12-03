from util import load_data, readlines_, timer
from collections import Counter, defaultdict
from functools import lru_cache


def parse_claim(claim):
    claim = claim.split()
    claim_id = int(claim[0][1:])
    origin = claim[2].split(',')
    origin = (int(origin[0]), int(origin[1][:-1]))
    size = tuple(int(i) for i in claim[3].split('x'))
    return (claim_id, origin, size)


@lru_cache(maxsize=1)
def make_grid(data):
    grid = Counter()
    for (id_, origin, size) in map(parse_claim, data):
        for x in range(size[0]):
            for y in range(size[1]):
                grid[(origin[0] + x, origin[1] + y)] += 1
    return grid


@timer
def part1(data):
    grid = make_grid(data)
    return sum(v >= 2 for v in grid.values())
        

@timer
def part2(data):
    grid = make_grid(data)

    for (id_, origin, size) in map(parse_claim, data):
        overlap = False
        for x in range(size[0]):
            for y in range(size[1]):
                if grid[(origin[0] + x, origin[1] + y)] > 1:
                    overlap = True
                    break
        if not overlap:
            return id_


def main():
    with load_data(day=3) as fp:
        data = tuple(readlines_(fp))

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
