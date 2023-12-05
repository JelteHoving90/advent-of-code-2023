def read_lines():
    file = open('input.txt', 'r')
    return file.readlines()


def main():
    total_sum = 0

    max = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    lines = read_lines()
    for line in lines:
        split = line.split(':')

        if len(split) != 2:
            continue

        # Find game index number
        game_idx = [int(x) for x in split[0].split() if x.isdigit()][0]

        # Find number of cubes
        rounds = [x.strip() for x in split[1].split(';')]

        valid = True

        for round in rounds:
            pulls = [x.strip() for x in round.split(',')]

            for pull in pulls:
                number = [int(x) for x in pull.split() if x.isdigit()][0]

                for color in max:
                    if color in pull and number > max[color]:
                        valid = False
                        break

        if valid:
            total_sum += game_idx

    print(total_sum)


if __name__ == "__main__":
    main()
