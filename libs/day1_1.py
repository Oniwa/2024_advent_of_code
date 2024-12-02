import pathlib as pl
from typing import List


def generate_two_lists(input_list: list[str]) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []

    for item in input_list:
        list1.append(int(item.split(' ')[0]))
        list2.append(int(item.split(' ')[1]))

    return list1, list2


def combine_lists(list1: list[int], list2: list[int]) -> list[list[int]]:
    combined_list = []

    if len(list1) == len(list2):
        for first, second in zip(list1, list2):
            combined_list.append([first, second])

    return combined_list


if __name__ == '__main__':
    input_data_file = pl.Path(r'c:\projects\adventofcode\data\day_1_1\input.txt')
    input_data_list = []

    with open(input_data_file, 'r') as f:
        for line in f:
            input_data_list.append(line)

    list_1, list_2 = generate_two_lists(input_data_list)

    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    combined_lists = combine_lists(sorted_list_1, sorted_list_2)

    diff_list = []
    for combined_item in combined_lists:
        diff_list.append(abs(combined_item[1] - combined_item[0]))

    sum_of_list = sum(diff_list)

    print(sum_of_list)
