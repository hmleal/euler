def is_lychrel(number, iteration=0):
    if iteration == 50:
        return (True, iteration)

    iteration += 1

    snumber = str(number)[::-1]
    number += int(snumber)

    if is_palindrome(number):
        return False, iteration

    return is_lychrel(number, iteration)


def is_palindrome(number):
    return number == int(str(number)[::-1])


def main():
    total = 0

    for x in range(1, 10001):
        is_, _ = is_lychrel(x)
        if is_:
            total += 1

    print(f"{total=}")


if __name__ == "__main__":
    main()
