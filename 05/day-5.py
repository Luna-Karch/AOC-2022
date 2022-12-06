def part_1():
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    stacks = data.split("\n\n")[0]

    mapped_stacks = {i: [] for i in range(1, 10)}

    for line in stacks.split("\n")[:-1]:
        for number, index in zip(range(1, 10), range(0, 33, 4)):
            mapped_stacks[number].append(line[index : index + 3].strip("[]")) if line[
                index : index + 3
            ].strip() else 0

    instructions = data.split("\n\n")[1].split("\n")

    for line in instructions:
        amount_to_move = int(line.lstrip("move ").split(" ")[0])
        original_stack = int(line.split("from ")[1].split(" ")[0])
        stack_to_move_to = int(line[::-1].split(" ")[0])
        mapped_stacks[stack_to_move_to] = (
            mapped_stacks[original_stack][:amount_to_move][::-1]
            + mapped_stacks[stack_to_move_to]
        )
        mapped_stacks[original_stack] = mapped_stacks[original_stack][amount_to_move:]

    return "".join([i[0] for i in mapped_stacks.values()])


def part_2():
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    stacks = data.split("\n\n")[0]

    mapped_stacks = {i: [] for i in range(1, 10)}

    for line in stacks.split("\n")[:-1]:
        for number, index in zip(range(1, 10), range(0, 33, 4)):
            mapped_stacks[number].append(line[index : index + 3].strip("[]")) if line[
                index : index + 3
            ].strip() else 0

    instructions = data.split("\n\n")[1].split("\n")

    for line in instructions:
        amount_to_move = int(line.lstrip("move ").split(" ")[0])
        original_stack = int(line.split("from ")[1].split(" ")[0])
        stack_to_move_to = int(line[::-1].split(" ")[0])
        mapped_stacks[stack_to_move_to] = (
            mapped_stacks[original_stack][:amount_to_move]
            + mapped_stacks[stack_to_move_to]
        )
        mapped_stacks[original_stack] = mapped_stacks[original_stack][amount_to_move:]

    return "".join([i[0] for i in mapped_stacks.values()])


print(part_1())
print(part_2())
