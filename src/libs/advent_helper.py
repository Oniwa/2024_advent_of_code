import pathlib as pl
import re


is_computation_enabled = True

def read_file_to_list(filename: pl.Path) -> list[str]:
    """
    Reads in a file and returns a list of strings
    :param filename: path to file
    :return: output_list is a list of strings
    """
    output_list = []

    with open(filename, 'r') as f:
        for line in f:
            output_list.append(line)

    return output_list


def generate_two_lists(input_list: list[str]) -> tuple[list[int], list[int]]:
    """
    Takes a list of strings with two values separated by 3 spaces and generates two lists of integers
    :param input_list: list of strings with two values separated by 3 spaces
    :return: two lists each containing a columns worth of data
    """
    list1 = []
    list2 = []

    for item in input_list:
        item_split = item.split('   ')
        list1.append(int(item_split[0]))
        list2.append(int(item_split[1]))

    return list1, list2


def combine_lists(list1: list[int], list2: list[int]) -> list[list[int]]:
    """
    Combines two lists into a single list

    :param list1: First list of ints
    :param list2:  Second list of ints
    :return: A list of lists; ie [[list1[0], list2[0], [list1[1], list2[1], ..., [list1[n], list2[n]]
    """
    combined_list = []

    if len(list1) == len(list2):
        for first, second in zip(list1, list2):
            combined_list.append([first, second])

    return combined_list


def is_report_safe(report:str) -> bool:
    """
    Checks if a report represents safe operating conditions

    :param report: A string of integers
    :return: True if safe; False otherwise
    """
    # Defaults to unsafe
    result = False

    # Splits string into a list of integers
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
                    break
        if not out_of_range:
            result = True

    return result


def generate_sub_reports(report:str) -> list[str]:
    """
    Takes a report string and generates a list of sub-reports.  Each sub report has one value removed from
    the original string.

    :param report: A string of integers
    :return: A list of strings of integers
    """
    sub_reports = []

    for index, value in enumerate(report.split(' ')):
        # Create working copy of initial report
        working_report_list = report.split(' ')

        # Removes a value at the indexed position and stores it as a sub report
        working_report_list.pop(index)
        sub_reports.append(' '.join(working_report_list))

    return sub_reports


def is_report_safe_with_dampener(report:str) -> bool:
    """
    Checks if a sub report represents safe operating conditions.  This represents a dampening effect of 1.

    :param report: String of integers
    :return: True if safe; False otherwise
    """
    result = False

    sub_report_list = generate_sub_reports(report)

    for report in sub_report_list:
        if is_report_safe(report):
            result = True
            break

    return result


def find_valid_instructions(memory_sequence: str) -> list[str]:
    """
    Finds valid instructions for a given memory sequence

    :param memory_sequence: Corrupted memory sequence
    :return: list of valid instructions
    """
    # Searches for a match of mul(0,0) to mul(999,999)
    regex = r"mul[(]\d{1,3},\d{1,3}[)]|do[(][)]|don[']t[(][)]"

    instruction_list = re.findall(regex, memory_sequence)

    return instruction_list


def evaluate_instruction(instruction:str) -> int | bool | None:
    """
    Evaluates an instruction

    :param instruction: Instruction string
    :return: Result of evaluation
    """
    result = None

    def mul(num1, num2):
        """
        Multiplies two numbers
        :param num1: First number
        :param num2: Second number
        :return: Multiplied result
        """
        return num1 * num2

    # Split the instruction into name and arguments
    func_parts = instruction.split('(')
    func_name = func_parts[0]
    args = func_parts[1].strip(')').split(',')

    # Call function
    if func_name == 'mul':
        func_to_call = eval(func_name)
        result = func_to_call(int(args[0]), int(args[1]))

    return result