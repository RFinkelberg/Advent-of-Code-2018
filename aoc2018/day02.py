from util import load_data, readlines_, timer
from collections import Counter


@timer
def part1(data):
    letter_counts = [Counter(word) for word in data]
    has_two = sum(1 for c in letter_counts if 2 in c.values())
    has_three = sum(1 for c in letter_counts if 3 in c.values())
    return has_two * has_three
        


@timer
def part2(data):
    data = sorted(data)
    for i in range(len(data) - 1):
        cur = data[i]
        next = data[i + 1]
        same = [cur[j] for j in range(len(cur)) if cur[j] == next[j]]
        if len(same) == len(cur) - 1:
            return ''.join(same)
        

def main():
    with load_data(day=2, part=1) as fp:
        data = readlines_(fp)

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
