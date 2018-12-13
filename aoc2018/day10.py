from util import load_data, readlines_, timer
from scipy.optimize import minimize
import numpy as np
import re


class Point:
    def __init__(self, pos, vel):
        self.pos = np.array(pos)
        self.vel = np.array(vel)

        
    def get_pos(self, t):
        return self.pos + t * self.vel


def make_grid(data):
    points = []
    for line in data:
        pos, vel = re.findall(r'(?<=<).*?(?=\>)', line)
        pos = list(map(int, pos.split(',')))
        vel = list(map(int, vel.split(',')))
        points.append(Point(pos, vel))
    
    def _bounding_box(t):
        pos = np.array([p.get_pos(t) for p in points])
        return np.ptp(pos[:, 0]) * np.ptp(pos[:, 1])

    msg_time = np.round(minimize(_bounding_box, np.array([0])).x)[0]

    pos = np.array([p.get_pos(msg_time) for p in points]).astype(int)
    xsize = np.ptp(pos[:, 0]).astype(int) + 1
    ysize = np.ptp(pos[:, 1]).astype(int) + 1

    grid = np.zeros((ysize, xsize)).astype(object)
    pos[:, 0] -= np.min(pos[:, 0])
    pos[:, 1] -= np.min(pos[:, 1])

    grid[grid == 0] = ' '
    grid[pos[:, 1], pos[:, 0]] = '*'
    return grid, msg_time


@timer
def part1(data):
    grid, _ = make_grid(data)
    return grid


@timer
def part2(data):
    _, time = make_grid(data)
    return time


def main():
    with load_data(day=10) as fp:
        data = readlines_(fp)

    grid, elapsed = part1(data)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            print(grid[i, j], end='')
        print('\n')
    print(elapsed)

    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
