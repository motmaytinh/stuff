import argparse

def recursive_fib(n):
    if n <=2:
        return 1
    return recursive_fib(n-2) + recursive_fib(n-1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculates n-th Fibonacci number.')
    parser.add_argument('integers', metavar='N', type=int, default=10, help='The nth fibonacci.')
    args = parser.parse_args()
    print(recursive_fib(args.integers))