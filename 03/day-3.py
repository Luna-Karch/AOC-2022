import string

priority_mappings = {v: i + 1 for i, v in enumerate(string.ascii_letters)}


def part_1():
    with open("day-3-input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    total_priority = 0

    for line in data:
        first_half = line[: len(line) // 2]
        second_half = line[len(line) // 2 :]
        result_letter = [item for item in first_half if item in second_half][0]
        total_priority += priority_mappings[result_letter]

    return total_priority


def part_2():
    with open("day-3-input.txt", "r", encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]

    total_priority = 0

    data = [data[x : x + 3] for x in range(0, len(data), 3)]
    for line in data:
        resulting_letter = [
            letter for letter in line[0] if letter in line[1] and letter in line[2]
        ][0]

        total_priority += priority_mappings[resulting_letter]

    return total_priority


print(part_1())
print(part_2())
