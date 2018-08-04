import argparse


def iterative_fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculates n-th Fibonacci number.')
    parser.add_argument('integers', metavar='N', type=int,
                        default=10, help='The nth fibonacci.')
    args = parser.parse_args()
    print(iterative_fib(args.integers))
