import libs.day1_1 as day1_1

def test_generate_two_lists():
    input_list = ['1 10\n', '2 20\n', '5 50\n', '3 30\n', '4 40\n', '6 60\n']

    list1, list2 = day1_1.generate_two_lists(input_list)

    expected_list_1 = [1, 2, 5, 3, 4, 6]
    expected_list_2 = [10, 20, 50, 30, 40, 60]

    assert list1 == expected_list_1
    assert list2 == expected_list_2
