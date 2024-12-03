import pathlib as pl
import src.libs.advent_helper as ah

input_path = pl.Path('../data/day_3/input.txt')
memory_sequence = ah.read_file_to_list(input_path)

memory_sequence = ''.join(memory_sequence)

instructions = ah.find_valid_instructions(memory_sequence)

result_list = []

for instruction in instructions:
    result_list.append(ah.evaluate_instruction(instruction))

sum_of_mults = sum(result_list)

print(f'Multiplication addition: {sum_of_mults}')

