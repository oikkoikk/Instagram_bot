class User:
    def __init__(self):
        self.__insta_email = "blahblah@naver.com"
        self.__insta_id = "blahblah@naver.com"
        self.__insta_password = "1234"
        self.__camp_id = "blahblah@naver.com"
        self.__camp_password = "1234"

    def getInstaEmail(self):
        return self.__insta_email

    def getInstaID(self):
        return self.__insta_id

    def getInstaPW(self):
        return self.__insta_password

    def getCampID(self):
        return self.__camp_id

    def getCampPW(self):
        return self.__camp_password
