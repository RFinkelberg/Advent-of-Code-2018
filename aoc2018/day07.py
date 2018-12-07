from util import load_data, readlines_, timer
import re
from collections import Counter, defaultdict


def make_graph(data):
    indegree = Counter()
    graph = defaultdict(list)
    for line in data:
        u = re.search(r'\w(?=\ must)', line).group()
        v = re.search(r'\w(?=\ can)', line).group()
        graph[u].append(v)
        if u not in indegree:
            indegree[u] = 0
        indegree[v] += 1

    return indegree, graph
    

@timer
def part1(data):
    # Topological sort
    indegree, graph = make_graph(data)
        
    sources = [k for k in indegree if indegree[k] == 0]
    order = []
    while sources:
        sources.sort()
        s = sources.pop(0)
        order.append(s)
        for v in graph[s]:
            indegree[v] -= 1
            if indegree[v] == 0:
                sources.append(v)
    return ''.join(order)


@timer
def part2(data):
    # Task scheduler
    indegree, graph = make_graph(data)

    sources = [k for k in indegree if indegree[k] == 0]
    done = set()
    t = 0
    workers = [None] * 4
    elapsed = [0] * 4
    duration = [0] * 4
    while len(done) != len(indegree):
        for i, worker in enumerate(workers):
            if workers[i] is not None:
                elapsed[i] += 1
                if elapsed[i] == duration[i]:
                    for v in graph[workers[i]]:
                        indegree[v] -= 1
                        if indegree[v] == 0:
                            sources.append(v)
                    done.add(workers[i])
                    workers[i] = None
            if workers[i] is None and sources:
                sources.sort()
                s = sources.pop(0)
                workers[i] = s
                elapsed[i] = 0
                duration[i] = 60 + ord(s) - 64
        t += 1
    return t - 1

    
def main():
    with load_data(day=7) as fp:
        data = tuple(readlines_(fp))

    print('Part 1: {}'.format(part1(data)))
    print('Part 2: {}'.format(part2(data)))


if __name__ == '__main__':
    main()
