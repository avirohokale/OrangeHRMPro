import configparser

config = configparser.RawConfigParser()

config.read("D:\\Avinash\\Testing\\Automation\\Practice\\OrangeHRMPro\\Configuration\\config.ini")


class Readvalue:

    @staticmethod
    def get_username():
        username = config.get('Login Info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Login Info', 'password')
        return password
