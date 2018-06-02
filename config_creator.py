import configparser
import os


def create_config(path):
    """
    Create a config file

    Ex Interpolation
        vars={"font": "Arial", "font_size": "100"}
    :param path:
    :return:
    """
    config = configparser.ConfigParser()

    config.add_section("TradeInfo")
    config.set("TradeInfo", "trade-file-path", "trades.txt")
    config.set("TradeInfo", "initial-capital", "500")
    config.set("TradeInfo", "maker-fee", "0.16")
    config.set("TradeInfo", "taker-fee", "0.26")
    config.set("TradeInfo", "slippage", "0.02")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Returns the config object
    :param path:
    :return:
    """
    if not os.path.exists(path):
        create_config()

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Print out a setting
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config = get_config(path)
    value = config.get(section,setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )

    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Update a setting
    :param path:
    :param section:
    :param setting:
    :param value:
    :return:
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    Delete a setting
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "./settings.ini"
    if not os.path.exists(path):
        create_config(path)