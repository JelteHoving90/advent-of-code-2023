import re


def read_lines():
    file = open('input.txt', 'r')
    return file.readlines()


def multiply_list(list):
    result = 1
    for x in list:
        result = result * int(x)
    return result


def is_gear(char):
    return char == '*'


def adjacent_to_gear(lines, line_idx, start_pos, end_pos):
    for pos in range(max(0, start_pos - 1), min(end_pos + 2, len(lines[line_idx]) - 1)):
        # Check line above
        if line_idx > 0:
            if is_gear(lines[line_idx - 1][pos]):
                return line_idx - 1, pos

        # Check line below
        if line_idx < len(lines) - 1:
            if is_gear(lines[line_idx + 1][pos]):
                return line_idx + 1, pos

    # Check same line before or after
    if start_pos > 0:
        if is_gear(lines[line_idx][start_pos - 1]):
            return line_idx, start_pos - 1

    if end_pos + 1 < len(lines[line_idx]) - 1:
        if is_gear(lines[line_idx][end_pos + 1]):
            return line_idx, end_pos + 1

    return False, False


def main():
    total_sum = 0
    lines = read_lines()
    gears = {}
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

                    # Get possible gear pos
                    gear_line, gear_pos = adjacent_to_gear(lines, idx, start_pos, end_pos)

                    # Gear on gear_line|gear_pos is adjacent to number
                    if gear_pos is not False and gear_line is not False:
                        # Get key for dict
                        gears_key = str(gear_line) + '.' + str(gear_pos)

                        # Check if item already exists
                        gear_numbers = gears[gears_key] if gears_key in gears else []

                        # Add new number to list
                        gear_numbers.append(number)

                        # Update dict
                        gears[gears_key] = gear_numbers

                    # Reset values
                    number = ''
                    start_pos = None

    # Calc gear ratios
    for gear in gears:
        if len(gears[gear]) == 2:  # Valid
            total_sum += multiply_list(gears[gear])

    print(total_sum)


if __name__ == "__main__":
    main()
