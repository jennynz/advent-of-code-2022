from count_calories import count_calories_per_elf
from calculate_score import calculate_total_score, calculate_shape

if __name__ == "__main__":
    print("Day 1")
    cals = count_calories_per_elf("inputs/day_1.txt")
    print(f"Part 1: {max(cals)} calories")
    cals_sorted = sorted(cals)
    TOP_N = 3
    print(f"Part 2: {sum(cals_sorted[-TOP_N:])} calories in top {TOP_N}")

    print("\nDay 2")
    total_score = calculate_total_score("inputs/day_2.txt")
    print(f"Part 1: {total_score} points")
    total_score_with_shape_calc = calculate_total_score("inputs/day_2.txt", True)
    print(f"Part 2: {total_score_with_shape_calc} points")
