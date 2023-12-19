from typing import List

with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


def process_history(line: str) -> List[int]:
    """
    Take a single line of the input data and turn it into an array of integers.
    """
    return [int(value) for value in line.split()]


test_processed_line = process_history(test_lines[0])
test_heavy_line = process_history(lines[0])


def generate_diff_line(processed_line: List[int]) -> List[int]:
    """
    Take a processed line (array of integers) and return the array of it's differences between
    each element
    """
    diffs = []
    for idx, value in enumerate(processed_line):
        if idx == len(processed_line) - 1:
            break
        else:
            diffs.append(processed_line[idx + 1] - value)
    return diffs


def generate_differences_matrix(
    diff_line: List[int], last_diffs: List[int] = [], first_run: bool = True
) -> List[List[int]]:
    """
    Recursively calc the differences array until you get a zero array, then return a matrix of
    all of the difference arrays.
    """
    diffs_matrix = [*last_diffs]
    if first_run:
        diffs_matrix.append(diff_line)
    if all(item == 0 for item in diff_line):
        return diffs_matrix
    else:
        diff = generate_diff_line(diff_line)
        diffs_matrix.append(diff)
        return generate_differences_matrix(
            diff_line=diff, last_diffs=diffs_matrix, first_run=False
        )


def extrapolate(difference_matrix: List[List[int]]) -> int:
    """
    Take a matrix of differences and extrapolate the next value in the history that generated the
    matrix. Return the extrapolated value as an integer.
    """
    reversed_matrix = difference_matrix[::-1]
    first = True
    for idx, diff_array in enumerate(reversed_matrix):
        if first:
            diff_array.append(0)
            previous_last_digit = diff_array[-1]
            first = False
        else:
            diff_array.append(diff_array[-1] + previous_last_digit)
            previous_last_digit = diff_array[-1]
            if idx == len(reversed_matrix) - 1:
                return previous_last_digit


def sum_extrapolations(input_data: List[str]) -> int:
    pass
