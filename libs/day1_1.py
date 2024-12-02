def generate_two_lists(input_list: list[str]) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []

    for item in input_list:
        list1.append(int(item[0].split(' ')[0]))
        list2.append(int(item[0].split(' ')[1]))

    return list1, list2

