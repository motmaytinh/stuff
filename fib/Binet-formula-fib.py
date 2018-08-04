from math import sqrt
import argparse


def fib(n): return int((((1+sqrt(5))**n)-((1-sqrt(5))**n))/((2**n)*sqrt(5)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculates n-th Fibonacci number.')
    parser.add_argument('integers', metavar='N', type=int,
                        default=10, help='The nth fibonacci.')
    args = parser.parse_args()
    print(fib(args.integers))
