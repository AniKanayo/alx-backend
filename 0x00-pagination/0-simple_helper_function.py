#!/usr/bin/env python3
"""Module for function index_range and pagination"""

import pandas as pd


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
    end_index = start_index + page_size
    return start_index, end_index


def paginate_data(page: int, page_size: int) -> pd.DataFrame:
    """
    Load data from CSV file and return a specific page

    Parameters:
    page (int): The current page
    page_size (int): The number of items per page

    Returns:
    pd.DataFrame: A DataFrame of the data for the desired page
    """
    # Load the data from the CSV file
    df = pd.read_csv('Popular_Baby_Names.csv')

    # Get the start and end indices for the desired page
    start_index, end_index = index_range(page, page_size)

    # Get the data for the desired page
    page_data = df.iloc[start_index:end_index]

    return page_data
