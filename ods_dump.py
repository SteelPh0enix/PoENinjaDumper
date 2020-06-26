import pyexcel_ods3
import sys
import os
from poeninja_dumper import load_all_categories, get_category_list, get_league, load_category

DEFAULT_OUTPUT_FILENAME = './PoENinjaData.ods'


def make_spreadsheet(file_name):
    sheet = {}
    if os.path.exists(file_name):
        sheet = pyexcel_ods3.get_data(file_name)

    for category_type in get_category_list():
        sheet.update({category_type: [['Item name', 'Value in chaos orbs']]})

    return sheet


def save_to_spreadsheet(file_name, data):
    pyexcel_ods3.save_data(file_name, data)


def run():
    print('League: {0}'.format(get_league()))

    ods_file_name = DEFAULT_OUTPUT_FILENAME
    if (len(sys.argv) >= 2):
        ods_file_name = sys.argv[1]

    print('Saving to/updating "{0}"\n'.format(ods_file_name))

    spreadsheet = make_spreadsheet(ods_file_name)

    for category_name, category_data in load_all_categories().items():
        category_data_list = [[name] + [value for key, value in data.items()] for name, data in category_data.items()]
        spreadsheet[category_name].extend(category_data_list)

    print('Saving the spreadsheet...')
    save_to_spreadsheet(ods_file_name, spreadsheet)


if __name__ == '__main__':
    run()
