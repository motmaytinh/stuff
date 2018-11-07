#Don't repeat your self or Single source of truth

def main():
    for i in range(101):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        if fizz and buzz:
            print("FizzBuzz")
        elif fizz:
            print("Fizz")
        elif buzz:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()