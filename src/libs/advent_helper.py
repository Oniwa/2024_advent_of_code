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
    result = False

    report_list = report.split()
    report_list = list(map(int, report_list))

    # Check to see if report is ascending or descending
    if report_list == sorted(report_list) or report_list == sorted(report_list, reverse=True):
        # Check that the distance between any two consecutive values is not 0 or greater than 4
        out_of_range = False
        for index, value in enumerate(report_list):

            if index > 0:
                distance = abs(report_list[index - 1] - report_list[index])
                if not (0 < distance < 4):
                    out_of_range = True
        if not out_of_range:
            result = True

    return result
