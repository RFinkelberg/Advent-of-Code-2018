from util import load_data, readlines_, timer
from collections import Counter, defaultdict
import re


def make_schedule(data):
    # chronological order
    data = sorted(data, key=lambda s: re.match(r'\[.*\]', s).group())

    schedule = defaultdict(Counter)
    current_guard = None
    start_t = 0
    for entry in data:
        guard_num = re.search(r'#\w*', entry)
        if guard_num is not None:
            # shift change
            current_guard = int(guard_num.group()[1:])
        else:
            minute = re.search(r':\d{2}', entry).group()
            minute = int(minute[1:])
            # guard falls asleep
            if entry[-2] == 'e':
                start_t = minute

            # guard wakes up
            if entry[-2] == 'u':
                for t in range(start_t, minute):
                    schedule[current_guard][t] += 1
    return schedule


@timer
def part1(data):
    schedule = make_schedule(data)
    sleepiest_guard = max(schedule, key=lambda k: sum(schedule[k].values()))
    return sleepiest_guard * schedule[sleepiest_guard].most_common(1)[0][0]


@timer
def part2(data):
    schedule = make_schedule(data)
    for guard in schedule:
        most_freq = schedule[guard].most_common(1)[0]
    most_freq = max(schedule, key=lambda k: schedule[k].most_common(1)[0][1])
    return most_freq * schedule[most_freq].most_common(1)[0][0]
    

def main():
    with load_data(day=4) as fp:
        data = tuple(readlines_(fp))

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
