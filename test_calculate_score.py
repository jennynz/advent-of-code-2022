from calculate_score import calculate_score, calculate_total_score, calculate_shape

INPUT_FILE = "test_inputs/day_2.txt"


def test_calculate_score():
    assert calculate_score("A", "Y") == 8
    assert calculate_score("B", "X") == 1
    assert calculate_score("C", "Z") == 6
    assert calculate_score("A", "Z") == 3


def test_calculate_total_score():
    assert calculate_total_score(INPUT_FILE) == 15


def test_calculate_total_score_with_shape_calc():
    assert calculate_total_score(INPUT_FILE, True) == 12


def test_calculate_shape():
    assert calculate_shape("A", "Y") == "X"
    assert calculate_shape("B", "X") == "X"
    assert calculate_shape("C", "Z") == "X"
    # They play Rock (A), you need to Win (Z), so you play Paper (Y)
    assert calculate_shape("A", "Z") == "Y"
