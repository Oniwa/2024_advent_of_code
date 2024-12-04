import pytest

import src.libs.advent_helper as ah


@pytest.mark.parametrize('search_string, expected_matches', [('MMMSXXMASM', 1),
                                                             ('MSAMXMSMSA', 1),
                                                             ('AMXSXMAAMM', 0),
                                                             ('MSAMASMSMX', 0),
                                                             ('XMASAMXAMM', 2),
                                                             ('XXAMMXXAMA', 0),
                                                             ('SMSMSASXSS', 0),
                                                             ('SAXAMASAAA', 0),
                                                             ('MAMMMXMMMM', 0),
                                                             ('MXMXAXMASX', 1),
                                                             ('XMASAMXMAS', 3)])
def test_find_xmas_count(search_string, expected_matches):
    # Given: A search string

    # When: ah.find_xmas_count is called
    actual_matches = ah.find_xmas_count(search_string)

    # Then: actual_matches SHALL equal expected_matches
    assert actual_matches == expected_matches
