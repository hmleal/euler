#!/usr/bin/env python


def main() -> str:
    result = 0
    for n in range(1, 1001):
        result += n ** n

    return str(result)[-10:]


if __name__ == "__main__":
    print(f"Result: {main()}")
