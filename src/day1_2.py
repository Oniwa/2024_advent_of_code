from collections import Counter
import pathlib as pl

from src.day1_1 import generate_two_lists
import src.libs.advent_helper as ah

if __name__ == '__main__':
    input_data_file = pl.Path(r'c:\projects\adventofcode\data\day_1_1\input.txt')
    input_data_list = []

    with open(input_data_file, 'r') as f:
        for line in f:
            input_data_list.append(line)

    list_1, list_2 = generate_two_lists(input_data_list)

    dict_of_repeated_elements = Counter(list_2)

    similarity_list = []

    for value in list_1:
        if value in dict_of_repeated_elements.keys():
            similarity_list.append(value * dict_of_repeated_elements[value])

    similarity_sum = sum(similarity_list)

    print(similarity_sum)
