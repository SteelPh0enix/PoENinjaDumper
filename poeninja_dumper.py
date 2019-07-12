import requests
import json
import pyexcel_ods
from datetime import date
import sys
import os

DEFAULT_OUTPUT_FILENAME = "PoENinjaData.ods"
POE_LEAGUE = "Betrayal"
TODAY_DATE = str(date.today())
POENINJA_URL_LIST = {
    "Currency": {
        "url": "https://poe.ninja/api/data/currencyoverview",
        "type": "Currency"
    },
    "Fragments": {
        "url": "https://poe.ninja/api/data/currencyoverview",
        "type": "Fragment"
    },
    "Scarabs": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "Scarab"
    },
    "Fossils": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "Fossil"
    },
    "Resonators": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "Resonator"
    },
    "Essences": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "Essence"
    },
    "DivinationCards": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "DivinationCard"
    },
    "Prophecies": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "Prophecy"
    },
    "SkillGems": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "SkillGem"
    },
    "BaseTypes": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "BaseType"
    },
    "HelmetEnchants": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "HelmetEnchant"
    },
    "UniqueMaps": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "UniqueMap"
    },
    "Maps": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "Map"
    },
    "UniqueJewels": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "UniqueJewel"
    },
    "UniqueFlasks": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "UniqueFlask"
    },
    "UniqueWeapons": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "UniqueWeapon"
    },
    "UniqueArmour": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "UniqueArmour"
    },
    "UniqueAccesories": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "UniqueAccessory"
    },
    "Beasts": {
        "url": "https://poe.ninja/api/data/itemoverview",
        "type": "Beast"
    }
}


def get_item_info(item_json, api_url):
    # Currency has other key names, don't ask why, i dunno
    if api_url == "https://poe.ninja/api/data/currencyoverview":
        return item_json["currencyTypeName"], item_json["chaosEquivalent"]
    else:
        return item_json["name"], item_json["chaosValue"]


def parse_item_page(json_data, item_data_info):
    page_data = list()
    for item in json_data["lines"]:
        item_name, item_value = get_item_info(item, item_data_info["url"])
        page_data.append([item_name, item_value])

    return page_data


def load_item_page(page_data):
    request_arguments = {"league": POE_LEAGUE,
                         "type": page_data["type"], "data": TODAY_DATE}
    data_request = requests.get(page_data["url"], params=request_arguments)

    return json.loads(data_request.text)


def make_spreadsheet(file_name):
    sheet = {}
    if os.path.exists(file_name):
        sheet = pyexcel_ods.get_data(file_name)
        for item_type in POENINJA_URL_LIST:
            sheet[item_type] = [["Item name", "Value in chaos orbs"]]
    else:
        for item_type in POENINJA_URL_LIST:
            sheet.update({item_type: [["Item name", "Value in chaos orbs"]]})

    return sheet


def save_to_spreadsheet(file_name, data):
    pyexcel_ods.save_data(file_name, data)


def run():
    print("League: {0}\nDate: {1}".format(POE_LEAGUE, TODAY_DATE))

    ods_file_name = DEFAULT_OUTPUT_FILENAME
    if (len(sys.argv) >= 2):
        ods_file_name = sys.argv[1]

    print("Saving to/updating '{0}'\n".format(ods_file_name))

    spreadsheet = make_spreadsheet(ods_file_name)

    for data_type, data in POENINJA_URL_LIST.items():
        print("Getting {0} prices...".format(data_type))

        item_data_json = load_item_page(data)
        parsed_data = parse_item_page(item_data_json, data)
        spreadsheet[data_type].extend(parsed_data)

    print("Saving the data to spreadsheet...")
    save_to_spreadsheet(ods_file_name, spreadsheet)


if __name__ == "__main__":
    run()
