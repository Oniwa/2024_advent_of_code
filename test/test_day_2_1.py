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
                                            ('1 3 6 7 9', True),
                                            ('29 28 27 25 26 25 22 20', True),
                                            ('7 10 8 10 11', True),
                                            ('48 46 47 49 51 54 56', True),
                                            ('1 1 2 3 4 5', True),
                                            ('1 2 3 4 5 5', True),
                                            ('5 1 2 3 4 5', True),
                                            ('1 4 3 2 1', True),
                                            ('1 6 7 8 9', True),
                                            ('1 2 3 4 3', True),
                                            ('9 8 7 6 7', True),
                                            ])
def test_is_report_safe_with_dampener(report: str, result: bool):
    assert ah.is_report_safe_with_dampener(report) == result


@pytest.mark.parametrize('report, result', [('7 6 4 2 1', ['6 4 2 1', '7 4 2 1', '7 6 2 1', '7 6 4 1', '7 6 4 2']),
                                            ('8 6 4 4 1', ['6 4 4 1', '8 4 4 1', '8 6 4 1', '8 6 4 1', '8 6 4 4']),])
def test_generate_sub_reports(report: str, result: list[str]):
    actual_sub_reports = ah.generate_sub_reports(report)

    assert actual_sub_reports == result
