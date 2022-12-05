def part_1():
    with open("day-1-input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    into_elves = [[int(i) for i in elf.split()] for elf in data.split("\n\n")]

    result = max(into_elves, key=sum)

    result = sum(result)

    return result


def part_2():
    with open("day-1-input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    into_elves = [[int(i) for i in elf.split()] for elf in data.split("\n\n")]

    all_sums = list(map(sum, into_elves))

    reversed_and_sorted = list(sorted(all_sums, reverse=True))
    return sum(reversed_and_sorted[:3])


print(part_1())
print(part_2())
