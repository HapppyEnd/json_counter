import ijson
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Tuple


def process_item(item: Dict[str, Any], count_items: defaultdict[str, int],
                 total_price: defaultdict[str, int]) -> None:
    """ Processes a single product item, updating the count and total
    price for the corresponding category.
    """
    category: str = item.get('category')
    price: float = item.get('price')
    count_items[category] += 1
    total_price[category] += price


def counter(file_path: Path) -> Tuple[Dict[str, int], Dict[str, float]]:
    """
    Counts the number of items and the total price for each category
    from a large JSON file.

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
            for item in ijson.items(f, 'item'):
                process_item(item, count_items, total_price)

    except FileNotFoundError:
        print(f'File {file_path} does not exist.')
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
