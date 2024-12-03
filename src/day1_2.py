from collections import Counter
import pathlib as pl

import src.libs.advent_helper as ah

if __name__ == '__main__':
    # Get data
    input_data_file = pl.Path(r'..\data\day_1_1\input.txt')
    input_data_list = []

    with open(input_data_file, 'r') as f:
        for line in f:
            input_data_list.append(line)

    # Separate data into two lists
    list_1, list_2 = ah.generate_two_lists(input_data_list)

    # Create a dictionary of counts of the values ie {1: 5, 2: 4, 5: 10} where key is the number and the value is the amount the number shows up
    dict_of_repeated_elements = Counter(list_2)

    # Find the similarity score
    similarity_list = []

    for value in list_1:
        if value in dict_of_repeated_elements.keys():
            # The score is calculated by multiplying the value by the number of time the value is in the list
            similarity_list.append(value * dict_of_repeated_elements[value])

    similarity_sum = sum(similarity_list)

    print(f'The similarity score is: {similarity_sum}')
