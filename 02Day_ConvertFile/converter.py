#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@ Date        : 01/08/2025 9:48 AM
@ Author      : Poco Ray
@ File        : converter.py
@ Description : Convert JSON file to CSV file
"""

import json

if __name__ == '__main__':
    try:
        with open("input.json", "r") as f:
            data = json.load(f)
            print(data)

            # Use keyword unpacking * to get the keys of the dictionary
            output = ','.join([*data[0]])
            print(output)

        for obj in data:
            output += '\n' + ','.join([str(obj[key]) for key in obj])

        with open("output.csv", "w") as f:
            f.write(output)
    except Exception as e:
        print(f'Error: {e}')
