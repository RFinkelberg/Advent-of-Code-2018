from util import load_data, readlines_, timer
from collections import deque
import re


"""Gross list solution
"""
# @timer
# def part1(data):
#     n_players = int(re.search(r'\d*(?=\ players)', data).group())
#     last_marble = int(re.search(r'\d*(?=\ points)', data).group())
    
#     board = [0]
#     scores = [0] * n_players
#     cur = 0
#     player = 0

#     for i in range(1, last_marble + 1):
#         if i % 23 == 0:
#             scores[player] += i
#             pop_idx = (cur - 7) % len(board)
#             removed = board.pop(pop_idx)
#             scores[player] += removed
#             cur = (pop_idx + 1) % len(board)
#         else:
#             push_idx = (cur + 1) % len(board) + 1
#             board.insert(push_idx, i)
#             cur = push_idx
#             player = (player + 1) % n_players
            
#     return max(scores)

"""Super fun deque solution
"""
@timer
def part1(data):
    n_players = int(re.search(r'\d*(?=\ players)', data).group())
    last_marble = int(re.search(r'\d*(?=\ points)', data).group())

    board = deque()
    board.append(0)
    scores = [0] * n_players

    for i in range(1, last_marble + 1):
        if i % 23:
            # maintain that the current marble is the last one in the queue
            board.rotate(-1)
            board.append(i)
        else:
            player = i % n_players
            scores[player] += i

            # push the 7th counterclockwise marble to the end and remove it
            board.rotate(7)
            scores[player] += board.pop()

            # set the current marble to the one after
            board.rotate(-1)
    return max(scores)
    

@timer
def part2(data):
    n_players = int(re.search(r'\d*(?=\ players)', data).group())
    last_marble = int(re.search(r'\d*(?=\ points)', data).group())
    last_marble *= 100

    board = deque()
    board.append(0)
    scores = [0] * n_players

    for i in range(1, last_marble + 1):
        if i % 23:
            # maintain that the current marble is the last one in the queue
            board.rotate(-1)
            board.append(i)
        else:
            player = i % n_players
            scores[player] += i

            # push the 7th counterclockwise marble to the end and remove it
            board.rotate(7)
            scores[player] += board.pop()

            # set the current marble to the one after
            board.rotate(-1)
    return max(scores)


def main():
    with load_data(day=9) as fp:
        data = fp.read().strip('\n')

    # data = '10 players; last marble is worth 1618 points'
    # data = '7 players; last marble is worth 25 points'
    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
