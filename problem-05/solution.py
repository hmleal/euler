def is_divisible(number):
    for x in range(1, 21):
        if number % x != 0:
            return False
    else:
        return True


def main():
    done = False
    number = 2520

    while not done:
        number += 10

        if is_divisible(number):
            done = True

    print(number)


if __name__ == "__main__":
    main()
