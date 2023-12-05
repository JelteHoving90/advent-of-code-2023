import re


def read_lines():
    file = open('input.txt', 'r')
    return file.readlines()


def transform_number_string(number, reverse):
    if reverse:
        number = number[::-1]

    if number.isdigit():
        return number

    number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    return number_dict[number]


def main():
    total_sum = 0

    regex = "one|two|three|four|five|six|seven|eight|nine"
    reversed_regex = regex[::-1]

    lines = read_lines()

    for line in lines:
        match = re.search("(" + regex + "|\d)", line)
        first_digit = transform_number_string(match.group(), False)

        match = re.search("(" + reversed_regex + "|\d)", line[::-1])
        last_digit = transform_number_string(match.group(), True)

        total_sum += int(first_digit + last_digit)

    print(total_sum)


if __name__ == "__main__":
    main()
