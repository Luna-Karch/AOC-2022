def part_1():
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    for index in range(3, len(data)):
        partial_string = data[index - 3 : index + 1]
        if len(set(partial_string)) == 4:
            return index + 1


def part_2():
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    for index in range(13, len(data)):
        partial_string = data[index - 13 : index + 1]
        if len(set(partial_string)) == 14:
            return index + 1


print(part_1())
print(part_2())
