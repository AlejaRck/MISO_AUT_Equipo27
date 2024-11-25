import yaml
import os
import json
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