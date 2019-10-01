LETTERS = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def main():
    with open("names.txt") as f:
        data = f.read()

    names = sorted([name.strip('"') for name in data.split(",")])

    final_score = 0
    for i, name in enumerate(names, start=1):
        final_score += score_name(name) * i

    print(final_score)


def score_name(name):
    # Faster than: sum([LETTERS[l] for l in name.lower()])
    final_score = 0
    for letter in name.lower():
        final_score += LETTERS[letter]

    return final_score


if __name__ == "__main__":
    main()
