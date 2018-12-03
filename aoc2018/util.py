from os.path import join
from contextlib import contextmanager
from typing import Sequence, IO
from functools import wraps
from time import time


@contextmanager
def load_data(day: int):
    """Read data from a given day

    Parameters
    ----------
    day : int 
    
    Yields
    ------
    A pointer to the file
    """
    day_num = 'day' + '0' + str(day) if day < 10 else 'day' + str(day)
    src_dir = join('../', 'inputs', day_num + '.txt')

    fp = open(src_dir, 'r')
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
