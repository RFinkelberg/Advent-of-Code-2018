from util import load_data, readlines_, timer
from scipy.spatial import KDTree
from functools import partial
from itertools import product
from collections import Counter, defaultdict


@timer
def part1(data):
    data = [tuple(map(int, s.split(','))) for s in data]

    min_x = min(x[0] for x in data)
    max_x = max(x[0] for x in data) 
    min_y = min(x[1] for x in data)
    max_y = max(x[1] for x in data)

    scores = Counter()
    is_finite = defaultdict(lambda: True)
    tree = KDTree(data)

    for pt in product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        dists, closest = tree.query(pt, k=2, p=1)
        if dists[0] != dists[1]:
            scores[data[closest[0]]] += 1
        if pt[0] in (min_x, max_x) or pt[1] in (min_y, max_y):
            is_finite[data[closest[0]]] = False

    highest = next(filter(lambda p: is_finite[p[0]], scores.most_common()))
    return highest[1]


@timer
def part2(data):
    data = [tuple(map(int, s.split(','))) for s in data]

    min_x = min(x[0] for x in data)
    max_x = max(x[0] for x in data) 
    min_y = min(x[1] for x in data)
    max_y = max(x[1] for x in data)

    score = 0
    tree = KDTree(data)

    query = partial(tree.query, k=len(data), p=1)
    score = sum(query(pt)[0].sum() < 10000 for pt in product(range(min_x, max_x + 1),
                                                             range(min_y, max_y + 1)))
    return score


def main():
    with load_data(day=6) as fp:
        data = tuple(readlines_(fp))
    # data = ('1, 1',
    #         '1, 6',
    #         '8, 3',
    #         '3, 4',
    #         '5, 5',
    #         '8, 9')

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
