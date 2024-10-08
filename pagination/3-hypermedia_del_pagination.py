#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Get a page from the dataset with resilience to deletion of items.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing pagination information.
        """
        # Validate that the index is in a valid range
        assert isinstance(index, int) and index >= 0, \
            "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)

        # Validate that the index is within the bounds of the dataset
        assert index < total_items, "Index out of range"

        data = []
        next_index = index
        count = 0

        # Iterate over the indexed dataset starting from the given index
        while count < page_size and next_index < total_items:
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
                count += 1
            next_index += 1

        # Prepare the hypermedia pagination dictionary
        hypermedia = {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index if next_index < total_items else None
        }

        return hypermedia
