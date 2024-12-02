import pathlib as pl


def generate_two_lists(input_list: list[str]) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []

    for item in input_list:
        list1.append(int(item.split(' ')[0]))
        list2.append(int(item.split(' ')[1]))

    return list1, list2


def combine_lists(list1: list[int], list2: list[int]) -> list[int]:
    return []


if __name__ == '__main__':
    input_data_file = pl.Path(r'c:\projects\adventofcode\data\day_1_1\input.txt')
    input_data_list = []

    with open(input_data_file, 'r') as f:
        for line in f:
            input_data_list.append(line)

    list_1, list_2 = generate_two_lists(input_data_list)

    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    diff_list = []


