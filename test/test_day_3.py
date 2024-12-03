import pytest

import src.libs.advent_helper as ah


@pytest.mark.parametrize('memory_sequence, instruction_list',
                         [(r'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))',
                           ['mul(2,4)',
                            'mul(5,5)',
                            'mul(11,8)',
                            'mul(8,5)']),])
def test_find_mul(memory_sequence: str, instruction_list: list[str]):
    # Given: A corrupted memory_sequence

    # When: find_valid_instructions is called
    actual_instructions = ah.find_valid_instructions(memory_sequence)

    # Then: actual_instructions SHALL equal intstruction_list
    assert actual_instructions == instruction_list
