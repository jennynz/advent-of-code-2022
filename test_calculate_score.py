from calculate_score import calculate_score, calculate_total_score

INPUT_FILE = "test_inputs/day_2.txt"


def test_calculate_score():
    assert calculate_score("A", "Y") == 8
    assert calculate_score("B", "X") == 1
    assert calculate_score("C", "Z") == 6


def test_calculate_total_score():
    assert calculate_total_score(INPUT_FILE) == 15
