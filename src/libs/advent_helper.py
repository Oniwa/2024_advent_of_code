import pathlib as pl


def read_file_to_list(filename: pl.Path) -> list:
    output_list = []

    with open(filename, 'r') as f:
        for line in f:
            output_list.append(line)

    return output_list


def generate_two_lists(input_list: list[str]) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []

    for item in input_list:
        item_split = item.split('   ')
        list1.append(int(item_split[0]))
        list2.append(int(item_split[1]))

    return list1, list2


def combine_lists(list1: list[int], list2: list[int]) -> list[list[int]]:
    combined_list = []

    if len(list1) == len(list2):
        for first, second in zip(list1, list2):
            combined_list.append([first, second])

    return combined_list


def is_report_safe(report:str) -> bool:
    result = None

    return result
