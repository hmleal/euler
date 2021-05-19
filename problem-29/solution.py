#!/usr/bin/env python


def main() -> int:
    result = set()

    for n in range(2, 101):
        for s in range(2, 101):
            result.add(n ** s)

    return len(result)


if __name__ == "__main__":
    print(f"Result: {main()}")
