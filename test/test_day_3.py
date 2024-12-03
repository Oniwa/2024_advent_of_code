import pytest

import src.libs.advent_helper as ah


@pytest.mark.parametrize('memory_sequence, instruction_list',
                         [(r'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))',
                           ['mul(2,4)',
                            'mul(5,5)',
                            'mul(11,8)',
                            'mul(8,5)']),
                          (r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
                           ['mul(2,4)',
                            "don't()",
                            'mul(5,5)',
                            'mul(11,8)',
                            'do()',
                            'mul(8,5)']),])
def test_find_valid_instructions(memory_sequence: str, instruction_list: list[str]):
    # Given: A corrupted memory_sequence

    # When: find_valid_instructions is called
    actual_instructions = ah.find_valid_instructions(memory_sequence)

    # Then: actual_instructions SHALL equal intstruction_list
    assert actual_instructions == instruction_list


@pytest.mark.parametrize('instruction, result', [('mul(2,4)', 8),
                                                 ('mul(5,5)', 25),
                                                 ('mul(11,8)', 88),
                                                 ('mul(8,5)', 40)])
def test_eval_instruction(instruction, result):
    # Given: a valid instruction

    # When: evaluate_instruction is called
    actual_result = ah.evaluate_instruction(instruction)

    # Then: actual_result SHALL equal result
    assert actual_result == result
