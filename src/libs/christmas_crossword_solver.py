import re


class ChristmasCrosswordSolver:
    def __init__(self, crossword):
        self.crossword = crossword
        self._cols = None
        self._rows = None
        self._forwards_diagonal = None
        self._backwards_diagonal = None
        self.num_matches = None

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