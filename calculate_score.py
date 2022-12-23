from typing import List

NUM_SHAPES = 3

SHAPE_SCORES = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

OUTCOME_SCORES = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0,
}


def calculate_score(opponent: str, you: str) -> int:
    score = SHAPE_SCORES[you]

    # Draw
    if SHAPE_SCORES[opponent] == SHAPE_SCORES[you]:
        score += OUTCOME_SCORES["DRAW"]

    # Win
    if SHAPE_SCORES[opponent] < SHAPE_SCORES[you] or (
        SHAPE_SCORES[you] == 1 and SHAPE_SCORES[opponent] == NUM_SHAPES
    ):
        score += OUTCOME_SCORES["WIN"]

    # Loss
    if SHAPE_SCORES[opponent] > SHAPE_SCORES[you] or (
        SHAPE_SCORES[you] == NUM_SHAPES and SHAPE_SCORES[opponent] == 1
    ):
        score += OUTCOME_SCORES["LOSE"]
    return score


def calculate_total_score(input_file: str) -> int:
    with open(input_file) as fp:
        lines = fp.readlines()
        total_score = 0
        for line in lines:
            inputs = line.split(" ")
            score = calculate_score(inputs[0], inputs[1].strip())
            total_score += score
    return total_score
