import configparser


class Constant:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("constant.ini")

        self.AUTHORIZED = self.config["Authentication parameters"]["AUTHORIZED"]


    def shanges(self, paragraph, value, importance):
        self.config.set(paragraph, value, importance)
        with open('constant.ini', 'w') as configfile:
            self.config.write(configfile)
