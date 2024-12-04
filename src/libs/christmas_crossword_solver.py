import re
from collections import defaultdict


class ChristmasCrosswordSolver:
    def __init__(self, crossword):
        self.crossword = crossword
        self._cols = None
        self._rows = None
        self._forwards_diagonal = None
        self._backwards_diagonal = None
        self.num_matches = None
        self._crossword_slicer()
        self._solve()

    @staticmethod
    def _find_xmas_count(search_string: str) -> int:
        """
        Finds all matchs of XMAS or SAMX (XMAS in reverse) in a search string.  The match can be part of a different match.
        IE: SAMXMAS matches both XMAS and SAMX and counts as 2 matches.
        :param search_string: String to search for matches
        :return: num_matches is the number of matches
        """
        xmas_regex = r'XMAS'
        samx_regex = r'SAMX'

        num_matches = 0

        num_matches += len(re.findall(samx_regex, search_string))
        num_matches += len(re.findall(xmas_regex, search_string))

        return num_matches

    def _crossword_slicer(self):
        working_crossword = []
        for row in self.crossword:
            working_crossword.append(list(row))

        max_col = len(working_crossword[0])
        max_row = len(working_crossword)
        rows = [[] for _ in range(max_col)]
        cols = [[] for _ in range(max_row)]
        fdiag = [[] for _ in range(max_row + max_col - 1)]
        bdiag = [[] for _ in range(len(fdiag))]
        min_bdiag = -max_row + 1

        for x in range(max_col):
            for y in range(max_row):
                rows[x].append(working_crossword[y][x])
                cols[y].append(working_crossword[y][x])
                fdiag[x + y].append(working_crossword[y][x])
                bdiag[x - y - min_bdiag].append(working_crossword[y][x])

        new_cols = []
        for row in cols:
            new_cols.append(''.join(row))

        new_rows = []
        for row in rows:
            new_rows.append(''.join(row))

        new_fdiag = []
        for diag in fdiag:
            diag.reverse()
            new_fdiag.append(''.join(diag))

        new_bdiag = []
        for diag in bdiag:
            new_bdiag.append(''.join(diag))

        self._cols = new_cols
        self._rows = new_rows
        self._forwards_diagonal = new_fdiag
        self._backwards_diagonal = new_bdiag

    def _solve(self):
        num_matches = 0

        for row in self._cols:
            num_matches += self._find_xmas_count(row)

        for row in self._rows:
            num_matches += self._find_xmas_count(row)

        for row in self._forwards_diagonal:
            num_matches += self._find_xmas_count(row)

        for row in self._forwards_diagonal:
            num_matches += self._find_xmas_count(row)

        self.num_matches = num_matches
