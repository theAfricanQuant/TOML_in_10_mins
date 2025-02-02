import tomllib
from pprint import pprint


def load_toml():
    """Load TOML data from
    the config.toml file
    """
    with open("config.toml", "rb") as file:
        toml_data = tomllib.load(file)
        return toml_data


if __name__ == "__main__":
    data: dict = load_toml()
    pprint(data, sort_dicts=False)
