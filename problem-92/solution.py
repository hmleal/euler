def find_next(number):
    if number == 89:
        return True

    if number == 1:
        return False

    res = sum([int(n) * int(n) for n in str(number)])

    return find_next(res)


def main(max_number):
    count = 0
    for n in range(1, max_number):
        if find_next(n):
            count += 1

    print(f"{count=}")


if __name__ == "__main__":
    main(10000000)
