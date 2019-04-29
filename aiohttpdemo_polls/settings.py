import os

import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
PROJECT_ROOT = BASE_DIR / 'aiohttpdemo_polls'
DEFAULT_CONFIG_PATH = BASE_DIR / 'config' / 'polls.yaml'
CONFIG_PATH = os.environ.get('CONFIG_PATH', DEFAULT_CONFIG_PATH)

def get_config(path):
    with open(path) as f:
        config = yaml.full_load(f)
    return config

CONFIG = get_config(CONFIG_PATH)
