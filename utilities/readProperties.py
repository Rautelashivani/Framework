import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getWronguseremail():
        wrongusername=config.get('common info', 'wrongusername')
        return wrongusername

    @staticmethod
    def getWrongpassword():
        wrongpassword=config.get('common info', 'wrongpassword')
        return wrongpassword