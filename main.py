from count_calories import count_calories_per_elf

if __name__ == "__main__":
    print("Day 1")
    cals = count_calories_per_elf("inputs/day_1.txt")
    print(f"Part 1: {max(cals)} calories")
    cals_sorted = sorted(cals)
    TOP_N = 3
    print(f"Part 2: {sum(cals_sorted[-TOP_N:])} calories in top {TOP_N}")

    print("\nDay 2")
