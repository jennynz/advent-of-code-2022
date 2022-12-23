from typing import List

NUM_SHAPES = 3

OPPONENT_SHAPE_SCORES = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}
YOUR_SHAPE_SCORES = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

OUTCOME_SCORES = {
    "WIN": 6,  # Z
    "DRAW": 3,  # Y
    "LOSE": 0,  # X
}
OUTCOME_LETTERS = {
    "Z": "WIN",
    "Y": "DRAW",
    "X": "LOSE",
}


def calculate_score(opponent: str, you: str) -> int:
    score = YOUR_SHAPE_SCORES[you]

    # Special cases at edge of circular list
    if YOUR_SHAPE_SCORES[you] == 1:
        if OPPONENT_SHAPE_SCORES[opponent] == NUM_SHAPES:
            return score + OUTCOME_SCORES["WIN"]
    if YOUR_SHAPE_SCORES[you] == NUM_SHAPES:
        if OPPONENT_SHAPE_SCORES[opponent] == 1:
            return score + OUTCOME_SCORES["LOSE"]

    # General cases for N shapes
    if OPPONENT_SHAPE_SCORES[opponent] < YOUR_SHAPE_SCORES[you]:
        return score + OUTCOME_SCORES["WIN"]
    if OPPONENT_SHAPE_SCORES[opponent] > YOUR_SHAPE_SCORES[you]:
        return score + OUTCOME_SCORES["LOSE"]
    return score + OUTCOME_SCORES["DRAW"]


def calculate_total_score(input_file: str, do_calculate_shape = False) -> int:
    with open(input_file) as fp:
        lines = fp.readlines()
        total_score = 0
        for line in lines:
            inputs = line.split(" ")
            opponent_shape = inputs[0]
            your_input = inputs[1].strip()
            if do_calculate_shape:
                your_shape = calculate_shape(opponent_shape, your_input)
                score = calculate_score(opponent_shape, your_shape)
            else:
                score = calculate_score(opponent_shape, your_input)
            # print(score)
            total_score += score
    return total_score


def calculate_shape(opponent: str, outcome_letter: str) -> str:
    outcome = OUTCOME_LETTERS[outcome_letter]

    # If the desired outcome is a DRAW, play the shape of the same value
    if outcome == "DRAW":
        return [
            k
            for k, v in YOUR_SHAPE_SCORES.items()
            if v == OPPONENT_SHAPE_SCORES[opponent]
        ][0]

    if outcome == "WIN":
        if opponent == "A":
            return "Y"
        if opponent == "B":
            return "Z"
        if opponent == "C":
            return "X"

    if outcome == "LOSE":
        if opponent == "A":
            return "Z"
        if opponent == "B":
            return "X"
        if opponent == "C":
            return "Y"
