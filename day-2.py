from __future__ import annotations


class DetermineChoice:
    def __init__(self, letter: str):
        self.letter = letter
        self.matching_table = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

        if self.letter in ("X", "A"):
            self.choice_name = "Rock"
            self.choice_points = 1
        elif self.letter in ("Y", "B"):
            self.choice_name = "Paper"
            self.choice_points = 2
        else:
            self.choice_name = "Scissors"
            self.choice_points = 3

    def __eq__(self, other: DetermineChoice) -> bool:
        return self.choice_name == other.choice_name

    def __gt__(self, other: DetermineChoice) -> bool:
        return self.matching_table[self.choice_name] == other.choice_name

    def __lt__(self, other: DetermineChoice) -> bool:
        return self.matching_table[
            self.choice_name
        ] != other.choice_name and not self.__eq__(other)


def part_1():
    with open("day-2-input.txt", "r", encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]

    total_score = 0

    for game in data:
        opponent_choice, your_choice = game.split()
        opponent_choice = DetermineChoice(opponent_choice)
        your_choice = DetermineChoice(your_choice)

        if opponent_choice == your_choice:
            total_score += your_choice.choice_points + 3
        elif your_choice > opponent_choice:
            total_score += your_choice.choice_points + 6
        else:
            total_score += your_choice.choice_points

    return total_score


print(part_1())
