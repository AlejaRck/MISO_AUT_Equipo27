import yaml
from e2e_playwright_45.metadata.path import Path


def get_config():
    with open(Path.config, encoding='utf8') as config_features:
        config = yaml.full_load(config_features)

    return  config