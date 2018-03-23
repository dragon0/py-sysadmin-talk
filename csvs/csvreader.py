#!/usr/bin/env python3

import csv

with open('MOCK_DATA.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['last_name'])

