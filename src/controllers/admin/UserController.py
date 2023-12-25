from src.controllers.BaseController import BaseController
import re
from src.models.users import User


class UserController(BaseController):

    def __init__(self):
        super().__init__(model=User)

    def checkExitsUser(self, username):
        sql = f"SELECT * FROM users WHERE username='{username}'"
        result = self.findFirstByQuery(sql)
        return result

    def checkExitsUserUpdate(self, username, user_id):
        sql = f"SELECT users.id FROM users WHERE username = '{username}' AND id != '{user_id}'"
        result = self.findFirstByQuery(sql)
        return result


    def checkUserEmailOrPhone(self, username: str):
        is_valid = ''
        if username.isdigit():
            if not self.isValidPhoneNumber(input_str=username):
                is_valid = 'Số điện thoại không đúng định dạng'
        elif username.find('@') != -1 and not self.isValidEmail(input_str=username):
            is_valid = 'Email không đúng định dạng'
        elif not self.isValidPhoneNumber(input_str=username) and not self.isValidEmail(input_str=username):
            is_valid = 'Vui lòng nhập email hoặc số điện thoại'
        return is_valid

    @staticmethod
    def isValidEmail(input_str):
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(email_pattern.match(input_str))

    @staticmethod
    def isValidPhoneNumber(input_str):
        phone_number_pattern = re.compile(r'^0\d{9}$')
        return bool(phone_number_pattern.match(input_str))

    def saveUser(self, user: User):
        return bool(self.insertData(user))

    def updateUser(self, user: User, user_id):
        return

    def updateUserWithModel(self, data, user_id):
        return self.updateDataWithModel(data, user_id)

    def login(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        sql = f"SELECT * FROM users WHERE username='{username}' and password = '{password}'"

        return self.connection.findFirstByQuery(sql)
