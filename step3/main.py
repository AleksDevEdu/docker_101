import time
import json

CONFIG_PATH = 'cfg/config.json'


def read_config(fpath):
    with open(fpath) as f:
        # read as dict
        config = json.load(f)

    return config


def main(config):
    # .get(key, default)
    name = config.get('name', '%DefaultName')
    while True:
        print(f'Hello World and {name}!')
        time.sleep(1)


if __name__ == '__main__':
    config = read_config(CONFIG_PATH)
    main(config)
