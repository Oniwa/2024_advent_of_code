import pathlib as pl

import src.libs.advent_helper as ah


if __name__ == '__main__':
    input_data_file = pl.Path(r'c:\projects\adventofcode\data\day_1_1\input.txt')

    input_data_list = ah.read_file_to_list(input_data_file)


    list_1, list_2 = ah.generate_two_lists(input_data_list)

    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    combined_lists = ah.combine_lists(sorted_list_1, sorted_list_2)

    diff_list = []
    for combined_item in combined_lists:
        diff_list.append(abs(combined_item[1] - combined_item[0]))

    sum_of_list = sum(diff_list)

    print(sum_of_list)
