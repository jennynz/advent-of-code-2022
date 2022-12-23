from typing import List


def count_calories_per_elf(input_file: str) -> List[int]:
    with open(input_file) as fp:
        lines = fp.readlines()
        elves_lst = []
        current_elf = []
        elf_count = 1
        for line in lines:
            if len(line.strip()) == 0:
                elf_calories = sum(current_elf)
                # print(f"Elf {elf_count}: {elf_calories}")
                elves_lst.append(elf_calories)
                current_elf = []  # Reset current elf
                elf_count += 1
                continue
            current_elf.append(int(line.strip()))

        # Gotta sum the last one as well
        elf_calories = sum(current_elf)
        # print(f"Elf {elf_count+1}: {elf_calories}")
        elves_lst.append(elf_calories)
    # print(f"Completed {len(elves_lst)} elves")
    return elves_lst
