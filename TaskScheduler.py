"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time
from typing import Callable


def print_func():
    print('Delay')


def delay_job_scheduler(f: Callable, n: int) -> None:
    time.sleep(float('0.%i' % n))
    f()


if __name__ == '__main__':
    delay_job_scheduler(print_func, 500)
