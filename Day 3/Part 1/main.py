import re


def read_lines():
    file = open('input.txt', 'r')
    return file.readlines()


def is_symbol(char):
    return char != '.' and not char.isdigit()


def adjacent_to_symbol(lines, line_idx, start_pos, end_pos):
    for pos in range(max(0, start_pos - 1), min(end_pos + 2, len(lines[line_idx]) - 1)):
        # Check line above
        if line_idx > 0:
            if is_symbol(lines[line_idx - 1][pos]):
                return True

        # Check line below
        if line_idx < len(lines) - 1:
            if is_symbol(lines[line_idx + 1][pos]):
                return True

    # Check same line before or after
    if start_pos > 0:
        if is_symbol(lines[line_idx][start_pos - 1]):
            return True

    if end_pos + 1 < len(lines[line_idx]) - 1:
        if is_symbol(lines[line_idx][end_pos + 1]):
            return True

    return False


def main():
    total_sum = 0
    lines = read_lines()
    for idx, line in enumerate(lines):

        number = ''
        start_pos = None

        for char_idx, char in enumerate(line):

            # Find numbers
            if char.isdigit():
                if start_pos is None:
                    start_pos = char_idx
                number += char
            else:
                if number != '':

                    # End current number
                    end_pos = char_idx - 1
                    if adjacent_to_symbol(lines, idx, start_pos, end_pos):
                        total_sum += int(number)

                    # Reset
                    number = ''
                    start_pos = None

    print(total_sum)


if __name__ == "__main__":
    main()
