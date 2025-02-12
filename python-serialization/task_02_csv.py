#!/usr/bin/env python3
"""
The programme will serialize csv file to json file
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    the function convert_csv_to_json
    """
    try:
        with open(csv_file, "r") as fi:
            Read_csv = csv.DictReader(fi)
            new_data = list(Read_csv)

        with open("data.json", "w") as j:
            json.dump(new_data, j)

        return True

    except FileNotFoundError:
        return False
