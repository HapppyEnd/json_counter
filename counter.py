import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple


def counter(file_path: Path) -> Tuple[Dict[str, int], Dict[str, int | float]]:
    """
    Counts the number of items and the total price for each category
    from a JSON file.

    Parameters:
    ----------
    file_path : Path
        The path to the JSON file containing product data.

    Returns:
    -------
    tuple
        A tuple of two dictionaries:
        - The first contains the count of items for each category.
        - The second contains the total sales amount for each category.
    """
    count_items: defaultdict[str, int] = defaultdict(int)
    total_price: defaultdict[str, int] = defaultdict(int)

    try:
        with open(file_path, 'r') as f:
            json_data: List[Dict[str, Any]] = json.load(f)

        for item in json_data:
            category: str = item.get('category')
            price: int | float = item.get('price')

            count_items[category] += 1
            total_price[category] += price

    except FileNotFoundError:
        print(f'File {file_path} does not exist.')
    except json.JSONDecodeError:
        print(f'File {file_path} is not a valid JSON.')
    except Exception as e:
        print(f'Error: {e}')
    else:
        return dict(count_items), dict(total_price)
    return {}, {}


if __name__ == '__main__':
    file_path = Path('f.json')
    items, price = counter(file_path)
    print(items)
    print(price)
