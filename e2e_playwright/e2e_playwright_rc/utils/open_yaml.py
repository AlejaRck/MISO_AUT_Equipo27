import yaml
import os
import json
import random
from faker import Faker
from e2e_playwright_rc.metadata.path import Path


def get_config():
    with open(Path.config, encoding='utf8') as config_features:
        config = yaml.full_load(config_features)

    return  config


def get_mockaroo_data(test_id:str, funcionanlidad:str):

    data_path = os.path.join(Path.input_mockaroo, funcionanlidad, f'{test_id}.json')
    with open(data_path, "r") as file:
        mockaroo_data = json.load(file)

    return mockaroo_data


def generate_random_data_tag(test_id:str):
    # Decide si usar datos de Mockaroo o Faker
    fake = Faker()
    data_mockaroo = get_mockaroo_data(test_id, 'tag')
    if random.choice([True, False]):
        return random.choice(data_mockaroo)
    else:
        return False