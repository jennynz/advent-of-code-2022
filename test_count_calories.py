from count_calories import count_calories_per_elf

INPUT_FILE = "test_inputs/day_1.txt"
ELVES_LIST = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
CALORIES_LIST = [6000, 4000, 11000, 24000, 10000]


def test_count_calories_per_elf():
    assert count_calories_per_elf(INPUT_FILE) == CALORIES_LIST
