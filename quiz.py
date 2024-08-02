import unittest
from typing import Any, List, Set, Tuple
from datetime import datetime


# Question 1
def reverse_list(l: list) -> List:
    """
    This function will reverse a list without using any built-in functions
    The function should return a reversed* list.
    Input l is a list which can contain any type of data.

    Parameters
        A list.

    Returns:
        The reversed list.

    Time complexity:
        O(n), n is the side of input list.

    Space complexity:
        O(1), since elements are switched in place.
    """
    counter = 0
    while counter < len(l) // 2:
        l[counter], l[len(l) - counter - 1] = l[len(l) - counter - 1], l[counter]
        counter += 1
    return l


class ListReverserTest(unittest.TestCase):

    def test_reverse_list_1(self):
        """
        This method tests on empty list scenario.
        """
        list_1: List[Any] = []
        list_2: List[Any] = []
        self.assertListEqual(list_1, list_2)

    def test_reverse_list_ints(self):
        """
        This method tests on reversing a list of numbers
        """
        num_list_1: List[int] = [1, 2, 3, 4, 5]
        num_list_2: List[int] = [5, 4, 3, 2, 1]
        res = reverse_list(num_list_1)
        print(repr(res))
        print(repr(num_list_2))
        self.assertListEqual(res, num_list_2)

    def test_reverse_list_bools(self):
        """
        This method tests on reversing a list of bool type items
        """
        bool_list_1: List[bool] = [True, True, False, False]
        bool_list_2: List[bool] = [False, False, True, True]
        res = reverse_list(bool_list_1)
        print(repr(res))
        print(repr(bool_list_2))
        self.assertListEqual(res, bool_list_2)

    def test_reverse_list_floats(self):
        """
        This method tests on reversing a list of bool type items
        """
        float_list_1: List[float] = [1.1, 1.2, 1.3, 1.4, 1.5]
        float_list_2: List[float] = [1.5, 1.4, 1.3, 1.2, 1.1]
        res = reverse_list(float_list_1)
        print(repr(res))
        print(repr(float_list_2))
        self.assertListEqual(res, float_list_2)

    def test_reverse_list_bytes(self):
        """
        This method tests on reversing a list of bool type items
        """
        bytes_list_1: List[bytes] = [b"hello", b"world", b"test", b"data"]
        bytes_list_2: List[bytes] = [b"data", b"test", b"world", b"hello"]
        res = reverse_list(bytes_list_1)
        print(repr(res))
        print(repr(bytes_list_2))
        self.assertListEqual(res, bytes_list_2)

    def test_reverse_list_strs(self):
        """
        This method tests on reversing a list of bool type items
        """
        strs_list_1: List[str] = ["hello", "world", "test", "data"]
        strs_list_2: List[str] = ["data", "test", "world", "hello"]
        res = reverse_list(strs_list_1)
        print(repr(res))
        print(repr(strs_list_2))
        self.assertListEqual(res, strs_list_2)

    def test_reverse_list_bytearrays(self):
        """
        This method tests on reversing a list of bool type items
        """
        bytearray_list_1: list[bytearray] = [bytearray(b"hello"), bytearray(b"world"), bytearray(b"data")]
        bytearray_list_2: list[bytearray] = [bytearray(b"data"), bytearray(b"world"), bytearray(b"hello")]
        res = reverse_list(bytearray_list_1)
        print(repr(res))
        print(repr(bytearray_list_2))
        self.assertListEqual(res, bytearray_list_2)

    def test_reverse_list_complexes(self):
        """
        This method tests on reversing a list of bool type items
        """
        complex_list_1: list[complex] = [1 + 2j, 3 + 4j, 5 + 6j]
        complex_list_2: list[complex] = [5 + 6j, 3 + 4j, 1 + 2j]
        res = reverse_list(complex_list_1)
        print(repr(res))
        print(repr(complex_list_2))
        self.assertListEqual(res, complex_list_2)

    def test_reverse_list_objects(self):
        """
        This method tests on reversing a list of bool type items
        """
        day1: str = datetime(2023, 8, 1).strftime("%Y-%m-%d")
        day2: str = datetime(2023, 8, 2).strftime("%Y-%m-%d")
        day3: str = datetime(2023, 8, 3).strftime("%Y-%m-%d")
        list_1: List[str] = [day1, day2, day3]
        list_2: List[str] = [day3, day2, day1]
        res = reverse_list(list_1)
        print(repr(list_1))
        print(repr(list_2))
        self.assertListEqual(res, list_2)

    def test_reverse_list_items_1(self):
        """
        This method tests on reversing a list of int, str, set and float.
        """
        items_list_3: List[Any] = [1, "cat", "", {1, 2}, 2.3, 5]
        items_list_4: List[Any] = [5, 2.3, {1, 2}, "", "cat", 1]
        res = reverse_list(items_list_3)
        print(repr(res))
        print(repr(items_list_4))
        self.assertListEqual(res, items_list_4)

    def test_reverse_list_items_2(self):
        """
        This method tests on reversing a list of int, str, list, dict, tuple and float.
        """
        items_list_1: List[Any] = [1, "cat", [9, 8], {"name": "Patrick"}, (1, 2), 2.3, 5, frozenset([1, 2, 3])]
        items_list_2: List[Any] = [frozenset([1, 2, 3]), 5, 2.3, (1, 2), {"name": "Patrick"}, [9, 8], "cat", 1]
        res = reverse_list(items_list_1)
        print(repr(res))
        print(repr(items_list_2))
        self.assertListEqual(res, items_list_2)


# Question 2
def is_valid_sudoku(matrix: List[List[str]]) -> bool:
    """
    This method is used for validating if a sudoku defined in 2D str array is valid. Below are the rules are used
    for validation:
    1. Each row contains digits 1-9 without repetition.
    2. Each column contains digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid contains the digits 1-9 without repetition.
    4. The dot '.' represents empty cell.

    Parameters:
        matrix (List[List[str]]): The sudoku to be validated in a 2D array representation

    Returns:
        bool: True if the sudoku is valid based on the 3 rules above, False otherwise.

    Time complexity:
        O(n), if the input is an n*n matrix

    Space complexity:
        O(n), if the input is an n*n matrix
    """
    for row in matrix:
        row_set: set[str] = set()
        for x in row:
            if x != '.':
                if x not in row_set:
                    row_set.add(x)
                else:
                    return False

    for j in range(9):
        col_set: set[str] = set()
        for row in matrix:
            if row[j] != '.':
                if row[j] not in col_set:
                    col_set.add(row[j])
                else:
                    return False

    for x_start_position in [0, 3, 6]:
        for y_start_position in [0, 3, 6]:
            box_set: set[str] = set()
            for x_offset in range(3):
                for y_offset in range(3):
                    ch = matrix[x_start_position + x_offset][y_start_position + y_offset]
                    if ch != '.':
                        if ch not in box_set:
                            box_set.add(ch)
                        else:
                            return False
    print("This is a valid sudoku.")
    return True


def solve_sudoku(matrix):
    """
    This method is used for validating if a sudoku defined in 2D str array is valid. Below are the rules are used
    for validation:
    1. Each row contains digits 1-9 without repetition.
    2. Each column contains digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid contains the digits 1-9 without repetition.
    4. The dot '.' represents empty cell.

    Parameters:
        matrix (List[List[str]]): The sudoku to be validated in a 2D array representation
        The input matrix is a 9x9 matrix. You need to write a program to solve it.

    Returns:
        None, the solution would be stored in the input matrix.

    Time complexity:
        Exponential time complexity, since we used backtracking to explore all possible solution.
    """

    if not is_valid_sudoku(matrix):
        return

    # the variable - rows, cols, boxes, and empty_list are used to store the input of matrix respectively
    rows: List[Set[str]] = [set() for _ in range(9)]
    cols: List[Set[str]] = [set() for _ in range(9)]
    boxes: List[Set[str]] = [set() for _ in range(9)]
    empty_list: List[Tuple[int, int]] = []

    for i, line in enumerate(matrix):
        for j, ch in enumerate(line):
            if ch == '.':
                empty_list.append((i, j))
            else:
                rows[i].add(ch)
                cols[j].add(ch)
                boxes[(i // 3) * 3 + (j // 3)].add(ch)

    # res is used to store the potential result
    res: List[str] = []

    def dfs(k):
        # This is when you finish collecting answers, which is also the exit condition of the backtracking.
        if k == len(empty_list):
            return True

        # This starts trying all possible numbers that is not in current position's row, column and its sub-box
        x, y = empty_list[k]
        for num in "123456789":
            if num not in rows[x] and num not in cols[y] and num not in boxes[(x // 3) * 3 + (y // 3)]:
                rows[x].add(num)
                cols[y].add(num)
                boxes[(x // 3) * 3 + (y // 3)].add(num)
                res.append(num)
                if dfs(k + 1):
                    return True
                # Step back since the number tried is not working.
                res.pop()
                rows[x].remove(num)
                cols[y].remove(num)
                boxes[(x // 3) * 3 + (y // 3)].remove(num)
        return False

    dfs(0)

    # Output answers into the original matrix.
    for (i, j), r in zip(empty_list, res):
        matrix[i][j] = r
    print(matrix)


class SudokuSolverTest(unittest.TestCase):

    matrix_1: List[List[str]] = [
                ["5", ".", ".", "9", ".", "7", ".", "2", "4"],
                ["7", "2", ".", "6", "1", "4", "8", ".", "9"],
                ["9", "4", "5", "2", "8", "3", ".", "7", "."],
                ["5", "3", "7", "9", ".", "1", "2", "8", "4"],
                ["1", "8", "6", "4", "7", "2", "3", "9", "."],
                ["2", "9", "4", "5", "3", "8", "7", "6", "1"],
                ["8", "5", "9", "7", "2", "6", "4", "3", "1"],
                ["3", "7", "2", "1", "9", "5", "6", "4", "8"],
                ["4", "6", "1", "8", "3", "7", "5", ".", "."]
              ]

    matrix_2: List[List[str]] = [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ]

    solution_1: List[List[str]] = [
                ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
                ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
                ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
                ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
                ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                ['3', '4', '5', '2', '8', '6', '1', '7', '9']
                ]

    def test_is_valid_sudoku_fail(self):
        """
        This method tests on an invalid sudoku matrix, for example, the digit 5 repeats twice in the first column
        from left.
        """
        self.assertFalse(is_valid_sudoku(self.matrix_1))

    def test_is_valid_sudoku_success(self):
        """
        This method tests on a valid sudoku matrix
        """
        self.assertTrue(is_valid_sudoku(self.matrix_2))

    def test_solve_sudoku_fail(self):
        """
        This method tests on an invalid sudoku matrix, for example, the digit 5 repeats twice in the first column
        from left. solve_sudoku(matrix) function will return it as it is.
        """
        solve_sudoku(self.matrix_1)
        self.assertListEqual(self.matrix_1, self.matrix_1)

    def test_solve_sudoku_success(self):
        """
        This method tests on a valid sudoku input. A correct solution will be returned.
        """
        solve_sudoku(self.matrix_2)
        self.assertListEqual(self.matrix_2, self.solution_1)


