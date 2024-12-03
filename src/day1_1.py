import pathlib as pl

import src.libs.advent_helper as ah


if __name__ == '__main__':
    # Get data
    input_data_file = pl.Path(r'..\data\day_1_1\input.txt')
    input_data_list = ah.read_file_to_list(input_data_file)

    # Separate data into two lists
    list_1, list_2 = ah.generate_two_lists(input_data_list)

    # Sort data
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    # Combine data into a single list; ie [[list1[0], list2[0], [list1[1], list2[1], ..., [list1[n], list2[n]]
    combined_lists = ah.combine_lists(sorted_list_1, sorted_list_2)

    # Create a list of the differences
    diff_list = []
    for combined_item in combined_lists:
        diff_list.append(abs(combined_item[1] - combined_item[0]))

    # Sum the differences
    sum_of_list = sum(diff_list)

    print(f'The total distance between the lists is: {sum_of_list}')
