import src.libs.advent_helper as ah

def test_generate_two_lists():
    # Given a list of strings with 2 columns separated by 3 spaces
    input_list = ['1   10\n', '2   20\n', '5   50\n', '3   30\n', '4   40\n', '6   60\n']

    # When: generate_two_lists is called
    list1, list2 = ah.generate_two_lists(input_list)

    # Then list1 SHALL equal expected_list_1 AND list2 SHALL equal expected_list_2
    expected_list_1 = [1, 2, 5, 3, 4, 6]
    expected_list_2 = [10, 20, 50, 30, 40, 60]

    assert list1 == expected_list_1
    assert list2 == expected_list_2


def test_combine_lists():
    # Given: 2 lists
    input1 = [1, 2, 3, 4, 5, 6]
    input2 = [10, 20, 30, 40, 50, 60]

    # When: combine_lists is called
    combined_list = ah.combine_lists(input1, input2)

    # Then: combined_list SHALL equal expected_list
    expected_list = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60]]
    assert combined_list == expected_list
