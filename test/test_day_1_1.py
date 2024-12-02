import libs.day1_1 as day1_1

def test_generate_two_lists():
    input_list = [['1 10'], ['2 20'], ['5 50'], ['3 30'], ['4 40'], ['6 60']]

    list1, list2 = day1_1.generate_two_lists(input_list)

    expected_list_1 = [1, 2, 5, 3, 4, 6]
    expected_list_2 = [10, 20, 50, 30, 40, 60]

    assert list1 == expected_list_1
    assert list2 == expected_list_2
