from os.path import join
from contextlib import contextmanager
from typing import Sequence, IO
from functools import wraps
from time import time


@contextmanager
def load_data(day: int, part: int):
    """Read data from a given day

    Parameters
    ----------
    day : int 
    
    part : int 
        whether to get part 1 (1) or part 2 (2)
    
    Yields
    ------
    A pointer to the file
    """
    day_num = 'day' + '0' + str(day) if day < 10 else 'day' + str(day)
    src_dir = join('../', 'inputs', day_num)

    assert part in (1, 2), 'Part argument must be 1 or 2'
    fname = 'p{}.txt'.format(part)

    fp = open(join(src_dir, fname), 'r')
    yield fp
    fp.close()


def readlines_(fp: IO[str]) -> Sequence[str]:
    """strips newlines and spaces from inputs
    """
    return [s.strip(' \n') for s in fp.readlines()]


def timer(func):
    """timing wrapper for a function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time()
        ret = func(*args, **kwargs)
        return ret, (time() - t0)
    return wrapper
