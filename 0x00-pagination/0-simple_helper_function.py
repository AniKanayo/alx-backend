#!/usr/bin/env python3
"""
This module contains the function index_range that takes
two integer arguments,page and page_size, and returns a
tuple of size two containing a start index and an end index
corresponding to the range of indexes to return in a list for
those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for pagination

    Parameters:
    page (int): The current page
    page_size (int): The number of items per page

    Returns:
    tuple: A tuple of the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
