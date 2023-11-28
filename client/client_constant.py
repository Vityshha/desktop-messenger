import configparser

config = configparser.ConfigParser()
config.read("constant.ini")

print(config["Network Parameters"]["SERVER"])