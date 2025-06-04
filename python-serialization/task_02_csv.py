#!/usr/bin/python3
"""
Module to convert CSV data to JSON format.

This module provides a function to read data from a CSV file
and serialize it into a JSON file named 'data.json'.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if conversion is successful, False if the file is not found.
    """
    try:
        with open(csv_filename, mode='r', newline='',
                  encoding='utf-8') as csv_file:
            data = list(csv.DictReader(csv_file))

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)
    except FileNotFoundError:
        return False

    return True
