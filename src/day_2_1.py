import pathlib as pl

import src.libs.advent_helper as ah

if __name__ == "__main__":
    # Get list of reports
    report_list = ah.read_file_to_list(pl.Path('../data/day_2_1/input.txt'))

    # Find number of safe reports with and without dampener
    safe_reports = 0
    safe_reports_with_dampener = 0

    for report in report_list:
        # Check to see if report is safe without dampener
        if ah.is_report_safe(report):
            safe_reports += 1
            safe_reports_with_dampener += 1
        else:
            # Check to see if report is safe with dampener
            if ah.is_report_safe_with_dampener(report):
                safe_reports_with_dampener += 1

    print(f'Safe reports without dampener: {safe_reports}')
    print(f'Safe reports with dampener: {safe_reports_with_dampener}')