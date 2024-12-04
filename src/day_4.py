import pathlib as pl

import src.libs.advent_helper as ah
import src.libs.christmas_crossword_solver as css


crossword_path = pl.Path('../data/day_4/crossword.txt')
crossword = ah.read_file_to_list(crossword_path)

solver = css.ChristmasCrosswordSolver(crossword)

print(f'There were {solver.num_matches} matches')