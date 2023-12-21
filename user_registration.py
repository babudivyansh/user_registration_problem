"""
@Author: Divyansh Babu

@Date: 2023-12-19 17:32

@Last Modified by: Divyansh Babu

@Last Modified time: 2023-12-19 17:32

@Title : User Registration Problem.
"""
import re
import logging
import sys

logging.basicConfig(filename='address_book_log.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m:%d:%y' '%I:%M:%S %p')
logger = logging.getLogger(__name__)

streamhdlr = logging.StreamHandler(sys.stderr)
logger.addHandler(streamhdlr)
streamhdlr.setLevel(logging.DEBUG)


class UserRegistration:
    def __init__(self, first_name, last_name, email, mobile_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self. mobile_number = mobile_number
        self.password = password

    def f_name_and_l_name_validation(self):
        """
        Description: This function validate first name and last name.
        Parameter: self object as parameter.
        Return: boolean value.
        """
        pattern = re.compile(r"^[A-Z][a-zA-Z]{2,}$")
        if pattern.match(self.first_name):
            return True
        elif pattern.match(self.last_name):
            return True
        else:
            return False

    def email_validation(self):
        """
        Description: This function validate email address.
        Parameter: self object as parameter.
        Return: boolean value.
        """
        pattern = re.compile(r"^[a-zA-Z]+(\.?[a-zA-Z0-9#$%&*-]+)?@[a-zA-Z]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$")
        if pattern.match(self.email):
            return True
        else:
            return False

    def mobile_number_validation(self):
        """
        Description: This function validate mobile number.
        Parameter: self object as parameter.
        Return: boolean value
        """
        pattern = re.compile(r'^(91 [6-9])[0-9]{9}$')
        if pattern.match(self.mobile_number):
            return True
        else:
            return False

    def password_validation(self):
        """
        Description: This function validate password.
        Parameter: self object as parameter.
        Return: boolean value
        """
        pattern = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*+,.<>?/:_;-]).{8,}$')
        if pattern.match(self.password):
            return True
        else:
            return False


if __name__ == '__main__':
    try:
        f_name = input("Enter valid first name: ")
        l_name = input("Enter valid last name: ")
        mail = input("Enter valid email: ")
        m_number = input("Enter valid mobile number: ")
        pws = input("Enter valid password: ")

        user_registration_obj = UserRegistration(f_name, l_name, mail, m_number, pws)
        print(user_registration_obj.f_name_and_l_name_validation())
        print(user_registration_obj.email_validation())
        print(user_registration_obj.mobile_number_validation())
        print(user_registration_obj.password_validation())

    except Exception as e:
        logger.exception(e)
