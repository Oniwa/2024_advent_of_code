import pytest

import src.libs.advent_helper as ah
import src.libs.christmas_crossword_solver as ccs


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
    actual_matches = ccs.ChristmasCrosswordSolver._find_xmas_count(search_string)

    # Then: actual_matches SHALL equal expected_matches
    assert actual_matches == expected_matches


@pytest.mark.parametrize('test_matrix, sub_matrices', [(['123', '456', '789', '0ab'],
                                                       {'cols': ['123', '456', '789', '0ab'],
                                                        'rows': ['1470', '258a', '369b'],
                                                        'forwards diagonal': ['1', '24', '357', '680', '9a', 'b'],
                                                        'backwards diagonal': ['0', '7a', '48b', '159', '26', '3'],
                                                       })])
def test_matrix_deconstruction(test_matrix: list, sub_matrices: dict):
    # Given: a test matrix

    # When: the test matrix is used to initialize a new instance of ChristmasCrosswordSolver
    solver = ccs.ChristmasCrosswordSolver(test_matrix)

    # Then: solver._cols SHALL equal sub_matrices['cols']
    assert solver._cols == sub_matrices['cols']

    # Then: solver._rows SHALL equal sub_matrices['rows']
    assert solver._rows == sub_matrices['rows']

    # Then: solver._forward_diagonal SHALL equal sub_matrices['forwards diagonal']
    assert solver._forwards_diagonal == sub_matrices['forwards diagonal']

    # Then: solver._backwards_diagonal SHALL equal sub_matrices['backwards diagonal']
    assert solver._backwards_diagonal == sub_matrices['backwards diagonal']

@pytest.mark.parametrize('test_matrix, expected_num_matches', [(['MMMSXXMASM',
                                                                 'MSAMXMSMSA',
                                                                 'AMXSXMAAMM',
                                                                 'MSAMASMSMX',
                                                                 'XMASAMXAMM',
                                                                 'XXAMMXXAMA',
                                                                 'SMSMSASXSS',
                                                                 'SAXAMASAAA',
                                                                 'MAMMMXMMMM',
                                                                 'MXMXAXMASX'], 18),
                                                               (['S..S..S',
                                                                '.A.A.A.',
                                                                '..MMM..',
                                                                'SAMXMAS',
                                                                '..MMM..',
                                                                '.A.A.A.',
                                                                'S..S..S'], 8),
                                                               (['A.A.A',
                                                                '.MMM.',
                                                                'AMXMA',
                                                                '.MMM.',
                                                                'A.A.A',], 0)
                                                               ])
def test_find_crossword_matches(test_matrix: list, expected_num_matches: int):
    # Given: A test matrix

    # When: the test matrix is used to initialize a new instance of ChristmasCrosswordSolver
    solver = ccs.ChristmasCrosswordSolver(test_matrix)

    # Then: solver.num_matches SHALL equal expected_num_matches
    assert solver.num_matches == expected_num_matches

