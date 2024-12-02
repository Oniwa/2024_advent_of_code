import pathlib as pl

import src.libs.advent_helper as ah

if __name__ == "__main__":
    report_list = ah.read_file_to_list(pl.Path('../data/day_2_1/input.txt'))

    safe_reports = 0

    for report in report_list:
        if ah.is_report_safe(report):
            safe_reports += 1

    print(safe_reports)

    safe_reports = 0

    for report in report_list:
        if ah.is_report_safe_with_dampener(report):
            safe_reports += 1

    print(safe_reports)