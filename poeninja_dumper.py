import requests
import json

POE_LEAGUE = 'Harvest'
POENINJA_URL_LIST = {
    'Currency': {
        'url': 'https://poe.ninja/api/data/currencyoverview',
        'type': 'Currency'
    },
    'Fragments': {
        'url': 'https://poe.ninja/api/data/currencyoverview',
        'type': 'Fragment'
    },
    'Incubators': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Incubator'
    },
    'Scarabs': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Scarab'
    },
    'Fossils': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Fossil'
    },
    'Resonators': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Resonator'
    },
    'Essences': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Essence'
    },
    'DivinationCards': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'DivinationCard'
    },
    'Prophecies': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Prophecy'
    },
    'SkillGems': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'SkillGem'
    },
    # Takes EXTREMELY long to download!
    # 'BaseTypes': {
    # 'url': 'https://poe.ninja/api/data/itemoverview',
    # 'type': 'BaseType'
    # },
    'HelmetEnchants': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'HelmetEnchant'
    },
    'UniqueMaps': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueMap'
    },
    'Maps': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Map'
    },
    'UniqueJewels': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueJewel'
    },
    'UniqueFlasks': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueFlask'
    },
    'UniqueWeapons': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueWeapon'
    },
    'UniqueArmour': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueArmour'
    },
    'UniqueAccesories': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueAccessory'
    },
    'Beasts': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Beast'
    }
}


def get_category_name(category_json, is_currency):
    # Currency has different key names than other categorys, don't ask why, i dunno
    if is_currency:
        return category_json['currencyTypeName']
    else:
        return category_json['name']


def get_category_chaos_value(category_json, is_currency):
    # Currency has different key names than other categorys, don't ask why, i dunno
    if is_currency:
        return category_json['chaosEquivalent']
    else:
        return category_json['chaosValue']


def parse_category(json_data, category_info):
    page_data = list()
    for category in json_data['lines']:
        is_currency = category_info['url'] == POENINJA_URL_LIST['Currency']['url']
        category_name = get_category_name(category, is_currency)
        category_value = get_category_chaos_value(category, is_currency)
        page_data.append([category_name, category_value])

    return page_data


def load_category(category_name):
    request_arguments = {'league': POE_LEAGUE,
                         'type': POENINJA_URL_LIST[category_name]['type'],
                         'language': 'en'}
    data_request = requests.get(
        POENINJA_URL_LIST[category_name]['url'], params=request_arguments)

    return json.loads(data_request.text)


def load_all_categories():
    category_dict = {}

    for category_name in POENINJA_URL_LIST:
        print('Downloading and parsing {0}'.format(category_name))
        category_dict[category_name] = load_category(category_name)

    return category_dict

def get_category_list():
  return [name for name in POENINJA_URL_LIST]

def get_league():
  return POE_LEAGUE