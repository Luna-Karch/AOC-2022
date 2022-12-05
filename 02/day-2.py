from __future__ import annotations


class DetermineShape:
    def __init__(self, letter: str):
        self.letter = letter
        self.matching_table = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

        if self.letter in ("X", "A", "Rock"):
            self.choice_name = "Rock"
            self.choice_points = 1
            self.needed_to_win = "Paper"
            self.needed_to_draw = "Rock"
            self.needed_to_lose = "Scissors"
        elif self.letter in ("Y", "B", "Paper"):
            self.choice_name = "Paper"
            self.choice_points = 2
            self.needed_to_win = "Scissors"
            self.needed_to_draw = "Paper"
            self.needed_to_lose = "Rock"
        else:
            self.choice_name = "Scissors"
            self.choice_points = 3
            self.needed_to_win = "Rock"
            self.needed_to_draw = "Scissors"
            self.needed_to_lose = "Paper"

    def __eq__(self, other: DetermineShape) -> bool:
        return self.choice_name == other.choice_name

    def __gt__(self, other: DetermineShape) -> bool:
        return self.matching_table[self.choice_name] == other.choice_name

    def __lt__(self, other: DetermineShape) -> bool:
        return self.matching_table[
            self.choice_name
        ] != other.choice_name and not self.__eq__(other)


def part_1():
    with open("day-2-input.txt", "r", encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]

    total_score = 0

    for game in data:
        opponent_choice, your_choice = game.split()
        opponent_choice = DetermineShape(opponent_choice)
        your_choice = DetermineShape(your_choice)

        if opponent_choice == your_choice:
            total_score += your_choice.choice_points + 3
        elif your_choice > opponent_choice:
            total_score += your_choice.choice_points + 6
        else:
            total_score += your_choice.choice_points

    return total_score


def part_2():
    with open("day-2-input.txt", "r", encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]

    outcome_mapping = {"X": "Lose", "Y": "Draw", "Z": "Win"}
    win_mapping = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

    total_score = 0

    for line in data:
        opponent_choice = DetermineShape(line[0])
        outcome_desired = outcome_mapping[line[-1]]

        if outcome_desired == "Lose":
            your_choice = DetermineShape(opponent_choice.needed_to_lose)
        elif outcome_desired == "Draw":
            your_choice = DetermineShape(opponent_choice.needed_to_draw)
        else:
            your_choice = DetermineShape(opponent_choice.needed_to_win)

        if opponent_choice == your_choice:
            total_score += your_choice.choice_points + 3
        elif your_choice > opponent_choice:
            total_score += your_choice.choice_points + 6
        else:
            total_score += your_choice.choice_points

    return total_score


print(part_1())
print(part_2())
