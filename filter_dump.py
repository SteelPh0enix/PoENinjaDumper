import os
import poeninja_dumper as dumper

# This is additional script, useful for making custom loot filters
# Dumps the poe.ninja content with certain price threshold

# Price thresholds in chaos
PRICE_THRESHOLDS = [1, 5, 10, 50, 100]
OUTPUT_DIR = './filterdata'


def split_items_data_into_categories(categories: list, items_data: dict):

    # We assume that data is sorted by value
    highest_price = next(iter(items_data.values()))['value']

    # We're going from lowest to highest tier
    actual_tier = 0
    categorized_data = [[]]
    for item in reversed(items_data):
        while actual_tier != len(categories) and items_data[item]['value'] > categories[actual_tier]:
            actual_tier += 1
            categorized_data.append([])
        categorized_data[actual_tier].append(item)

    return categorized_data


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    print('League: {0}'.format(dumper.get_league()))
    print('Downloading poe.ninja content... ')
    categories_data = dumper.load_all_categories()
    print('Content downloaded!')

    for category, data in categories_data.items():
        categorized_data = split_items_data_into_categories(
            PRICE_THRESHOLDS, data)
        category_i = 0
        category_file_path = os.path.join(OUTPUT_DIR, category + '.txt')
        print('Putting {1} data in {0}'.format(category_file_path, category))

        with open(category_file_path, 'w') as category_file:
            for category_items in categorized_data:
                tier_content = ' '.join(['"' + x + '"' for x in category_items])
                category_file.write('Tier #{0}:\n{1}\n'.format(category_i, tier_content))
                category_i += 1


if __name__ == '__main__':
    main()
