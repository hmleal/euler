CACHE = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
}


def _parse_dozens(number: str) -> str:
    if number[0] == "0":
        number = number[1]

    if number in CACHE:
        return CACHE[number]

    part_one = CACHE[number[0] + "0"]
    part_two = CACHE[number[1]]

    return f"{part_one}{part_two}"


def main():
    letters = ""

    for x in range(1, 1000):
        num = str(x)

        if num in CACHE:
            letters += CACHE[num]
            continue

        if len(num) == 2:
            letters += _parse_dozens(num)
            continue

        if len(num) == 3:
            part_one = CACHE[num[0]] + "hundred"
            if num[1:] == "00":
                letters += part_one
            else:
                part_two = _parse_dozens(num[1:])
                letters += f"{part_one}and{part_two}"
            continue

    return letters


if __name__ == "__main__":
    letters = main() + "onethousand"
    print(len(letters))
