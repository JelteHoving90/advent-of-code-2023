def read_lines():
    file = open('input.txt', 'r')
    return file.readlines()


def main():
    total_sum = 0
    first_digit = last_digit = ''
    lines = read_lines()
    for line in lines:
        for char in line:
            if char.isdigit():
                first_digit = char
                break
        for char in line[::-1]:
            if char.isdigit():
                last_digit = char
                break
        total_sum += int(first_digit + last_digit)
    print(total_sum)


if __name__ == "__main__":
    main()
