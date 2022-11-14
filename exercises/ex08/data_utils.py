"""Dictionary related utility functions."""


__author__ = "730482280"


# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(input_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = dict()
    for heading in input_table:
        storage_list = list()
        for value in input_table[heading]:
            if n <= 0:
                break
            storage_list.append(value)
            if len(storage_list) == n:
                break
        result[heading] = storage_list
    return result


def select(input_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = dict()
    for desired_column in columns:
        if desired_column in input_table:
            result[desired_column] = input_table[desired_column]
    return result


def concat(input_table_1: dict[str, list[str]], input_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = dict()
    for column in input_table_1:
        result[column] = input_table_1[column]
    for column in input_table_2:
        if column in result:
            result[column] += input_table_2[column]
        else:
            result[column] = input_table_2[column]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Takes an input list and creates a dictionary in which the list values are the values and the position in the list is the key."""
    output_dict: dict[str, int] = dict()
    for value in input_list:
        if value in output_dict:
            output_dict[value] += 1
        else:
            output_dict[value] = 1
    return output_dict