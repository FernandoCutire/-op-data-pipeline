import yaml

___config = None


def config():
    if not ___config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.load(f, Loader=yaml.FullLoader)
    return __config
