import os
import poeninja_dumper as dumper

# This is additional script, useful for making custom loot filters
# Dumps the poe.ninja content with certain price threshold

# Price thresholds in chaos
PRICE_THRESHOLDS = [1, 5, 10, 50, 100]
OUTPUT_DIR = './filterdata'

def split_data_into_categories(categories, data):
  data = {}
  # We assume that data is sorted by value

  highest_price =

  return data

def main():
  if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

  print('League: {0}'.format(dumper.get_league()))
  print('Downloading poe.ninja content... ', end='')
  categories_data = dumper.load_all_categories()
  print('downloaded!')

  for category, data in categories_data.items():
    print('Parsing {0}'.format(category))



if __name__ == '__main__':
  main()