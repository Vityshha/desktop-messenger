import configparser


class Constant:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("constant.ini")

        self.HEADER = self.config["Network Parameters"]["HEADER"]
        self.PORT = self.config["Network Parameters"]["PORT"]
        self.SERVER = self.config["Network Parameters"]["SERVER"]
        self.FORMAT = self.config["Network Parameters"]["FORMAT"]
        self.DISCONNECT_MESSAGE = self.config["Network Parameters"]["DISCONNECT_MESSAGE"]
        self.ADDR = (self.SERVER, self.PORT)

        self.AUTHORIZED = self.config["Authentication parameters"]["authorized"]
        self.id = self.config["Authentication parameters"]["id"]
        self.login = self.config["Authentication parameters"]["login"]

    def shanges(self, paragraph, value, importance):
        self.config.set(paragraph, value, importance)
        with open('constant.ini', 'w') as configfile:
            self.config.write(configfile)
