def part_1():
    with open("input.txt", "r", encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]

    total_overlaps = 0

    for line in data:
        range_one, range_two = line.split(",")
        range_one_start, range_one_end = map(int, range_one.split("-"))
        range_two_start, range_two_end = map(int, range_two.split("-"))

        if range_one_start <= range_two_start and range_one_end >= range_two_end:
            total_overlaps += 1
        elif range_two_start <= range_one_start and range_two_end >= range_one_end:
            total_overlaps += 1
        else:
            total_overlaps += 0

    return total_overlaps


def part_2():
    with open("input.txt", "r", encoding="utf-8") as f:
        data = [i.strip() for i in f.readlines()]

    total_overlaps = 0

    for line in data:
        range_one, range_two = line.split(",")
        range_one_start, range_one_end = map(int, range_one.split("-"))
        range_two_start, range_two_end = map(int, range_two.split("-"))
        the_range_one = list(range(range_one_start, range_one_end + 1))
        the_range_two = list(range(range_two_start, range_two_end + 1))
        if [item for item in the_range_one if item in the_range_two]:
            total_overlaps += 1

    return total_overlaps


print(part_1())
print(part_2())
