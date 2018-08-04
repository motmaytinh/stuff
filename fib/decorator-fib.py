import argparse
import functools


@functools.lru_cache()
def fib_lru_cache(n):
    if n < 2:
        return n
    else:
        return fib_lru_cache(n - 2) + fib_lru_cache(n - 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculates n-th Fibonacci number.')
    parser.add_argument('integers', metavar='N', type=int,
                        default=10, help='The nth fibonacci.')
    args = parser.parse_args()
    print(fib_lru_cache(args.integers))
