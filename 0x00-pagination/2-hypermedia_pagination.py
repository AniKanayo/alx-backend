#!/usr/bin/env python3
"""
This module handles pagination for a dataset within the Server class.
"""

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
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

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader]
                self.__dataset = self.__dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset.

        Parameters:
        page (int): The current page. Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

        Returns:
        List[List]: The appropriate page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns dictionary of pagination data.

        Parameters:
        page (int): The current page. Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

        Returns:
        dict: A dictionary of pagination parameters and data
        """
        total_pages = math.ceil(len(self.__dataset) / page_size)
        data = self.get_page(page, page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
