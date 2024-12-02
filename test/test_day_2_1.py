import src.libs.advent_helper as ah

import pytest

@pytest.mark.parametrize('report, result', [('7 6 4 2 1', True),
                                            ('1 2 7 8 9', False),
                                            ('9 7 6 2 1', False),
                                            ('1 3 2 4 5', False),
                                            ('8 6 4 4 1', False),
                                            ('1 3 6 7 9', True)])
def test_is_report_safe(report: str, result: bool):
    assert ah.is_report_safe(report) == result


@pytest.mark.parametrize('report, result', [('7 6 4 2 1', True),
                                            ('1 2 7 8 9', False),
                                            ('9 7 6 2 1', False),
                                            ('1 3 2 4 5', True),
                                            ('8 6 4 4 1', True),
                                            ('1 3 6 7 9', True)])
def test_is_report_safe_with_dampener(report: str, result: bool):
    assert ah.is_report_safe_with_dampener(report) == result