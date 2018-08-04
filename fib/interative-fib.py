import argparse


def iterative_fib(n):
    f1 = 1
    f2 = 1
    if n <= 2:
        return f1
    f3 = f2 + f1
    for n in range(3, n, 1):
        f1 = f2
        f2 = f3
        f3 = f2 + f1
    return f3


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculates n-th Fibonacci number.')
    parser.add_argument('integers', metavar='N', type=int,
                        default=10, help='The nth fibonacci.')
    args = parser.parse_args()
    print(iterative_fib(args.integers))
