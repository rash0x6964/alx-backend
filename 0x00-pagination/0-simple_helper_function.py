#!/usr/bin/env python3
""" A module contains a pagination helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ Returns a tuple containing the start  andend index for pagination. """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
