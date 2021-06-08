import math


def main():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = (a ** 2) + (b ** 2)
            c = math.sqrt(c)
            if a + b + c == 1000:
                return a * b * c


if __name__ == "__main__":
    print(f"Result: {main()}")
