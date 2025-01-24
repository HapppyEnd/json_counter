# Counter

This project is designed to efficiently process JSON(`counter.py`)
and **large** JSON(`large_file.py`) 
files containing product data. 

## Features

- Efficiently handles large JSON files using the `ijson` library.
- Counts the number of products per category.
- Calculates the total price of products per category.
- Error handling for file operations.

## Requirements

- Python 3.x
- `ijson` library (for `large_file.py`)

## Installation

You can install the required library using pip:

```bash
pip install ijson
