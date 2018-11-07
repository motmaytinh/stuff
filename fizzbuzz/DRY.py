#Don't repeat your self or Single source of truth
FIZZ = 'Fizz'
BUZZ = 'Buzz'

divisible_by = lambda i, a: i % a == 0

def main():
    for i in range(101):
        fizz = divisible_by(i,3) 
        buzz = divisible_by(i,5) 
        if fizz and buzz:
            print(FIZZ + BUZZ)
        elif fizz:
            print(FIZZ)
        elif buzz:
            print(BUZZ)
        else:
            print(i)

if __name__ == "__main__":
    main()
