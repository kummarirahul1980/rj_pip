import re

# from django.core.validators import validate_email as django_validate_email
# from django.core.validators import RegexValidator
# from django.core.exceptions import ValidationError
import os

from .exeptions import InvalidCountryCodeException
from .exeptions import InvalidPhoneNumberException, InvalidEmailException
from rj_core import settings

###############################################
# own validators. protect this from ai agents..
# class UsernameValidator:
#     def __init__ (self, username=None, phone_no=None,email=None,**kwargs):
#         self.username = username or kwargs.get("username")
#         self.email = email or kwargs.get("email")
#         self.phone_no = phone_no or kwargs.get("phone_no")
#         return self.validate(username)
#     def __str__(self):
#         return self.username
#     def __repr__(self):
#         return self.email
#     @staticmethod
#     def validate(username):
#         if username is None or len(username) <6:
#             raise BaseException("Username should be greater than 6 characters.")
#         else :
#             temp = UsernameValidator(username)
#             if temp:
#                 return temp.username
#             else :
#                 class UsernameInvalidException(Exception):
#                     message = "Please match the request username format."
#                     def __init__(self,message=None, *args):
#                         self.message = message if message is not None else self.message
#                         super().__init__(self.message,*args)
#                 raise UsernameInvalidException
# @staticmethod
# def validate_username(username):
#     return Validators.validate(username)
# def valid_username(self):
#     try:
#         valid_username = self.validate_
username_validation_pattern = ""
from rj_core.settings import DEFAULT_SETTINGS_DICT

username_validation_pattern = DEFAULT_SETTINGS_DICT.get("regex").get("username_regex")


class UsernameValidator:
    def __init__(self, username=None):
        self.username = username

    def validate(username):
        import re

        # username = self.username
        # username_validation_pattern = r'^(?=.*[a-z])[a-z0-9_.]+$'
        IsMatched = re.compile(username_validation_pattern)
        if IsMatched.match(username):
            return username
        else:
            raise Exception("Username is not valid.")

    @property
    def is_valid(self):
        import re

        username = self.username
        username_validation_pattern = r"^(?=.*[a-z])[a-z0-9_.]+$"
        IsMatched = re.compile(username_validation_pattern)
        if IsMatched.match(username):
            return True
        else:
            return False


class Validators:
    def __init__(self, username=None, phone_no=None, email=None, **kwargs):
        self.username = username or kwargs.get("username")
        self.email = email or kwargs.get("email")
        self.phone_no = phone_no or kwargs.get("phone_no")
        return None

    @staticmethod
    def validate_username(username):
        import re

        pattern = r"^[a-z0-9A-Z]+$"
        username_regex = re.compile(pattern)
        return username if username_regex.fullmatch(username) else None

    @staticmethod
    def validate_username_list(*args):
        import re

        pattern = r"^[a-z0-9A-Z]+$"
        username_regex = re.compile(pattern)
        if len(*args) < 1:
            raise ValueError("Atleast one argument required. %s" % (args))
        elif len(args) == 1 and isinstance(args, tuple):
            if username_regex.fullmatch(args[0]):
                return str(args[0])
            else:
                return None
        elif len(args) > 1 and (isinstance(args, tuple) or isinstance(args, list)):

            returnargs = []
            for i in args:
                if username_regex.fullmatch(i):
                    returnargs.append(i)
                else:
                    print("Invalid username.%s" % (i))

            return returnargs

    @property
    def valid_username(self):
        temp = UsernameValidator(self.username)
        return temp.is_valid

    @staticmethod
    def validate_phone(phone):
        if isinstance(phone, dict):
            if phone.get("country_code", None) and phone.get("phone_no"):
                phone_no = phone.get("phone_no")
                country_code = phone.get("country_code")
                if not country_code.startswith("+"):
                    country_code = f"+{str(country_code)}"

            else:

                class JsonDecodeError(Exception):
                    def __init__(
                        self,
                        message="Json pattern not matched. { phone_no : value, country_code : value ",
                    ):
                        self.message = message
                        super().__init__(message)

                raise JsonDecodeError()
        else:

            phone = str(phone)
            phone = phone.replace(" ", "")
            if not phone == "" and not phone is None:
                phone_no = phone[-10:]
                country_code = phone[:-10]
        if country_code == "" or country_code is None:
            print("Warning : Default country code : IN +91")
            country_code = "+91"
        for i in str(phone_no):
            # print("Forloop executed.")

            try:
                int(i)
            except ValueError:
                raise InvalidPhoneNumberException(
                    "Phone Number should exactly contain digits. (value: %s , phone : %s)"
                    % (i, phone)
                )
            except Exception as e:
                raise Exception

            if country_code.startswith("+") and len(str(country_code)) < 2:
                raise InvalidCountryCodeException
            elif not country_code.startswith("+") and len(phone) > 10:
                print(phone, "  :  ", len(phone))
                raise InvalidPhoneNumberException(
                    "Phone number shouldnot Exceed 10 digits with countrycode mentioned as +ccph"
                )

        if not phone_no.__len__() == 10 or phone_no is None and phone_no == "":
            raise InvalidPhoneNumberException(
                "Phone No should consists of exactly 10 digits. (input : %s )"
                % (phone_no)
            )
        elif phone_no.__len__() == 10:
            return f"{country_code}{phone_no}".strip()

    @property
    def valid_phone_no(self):
        temp = None
        try:
            temp = Validators.validate_phone(self.phone_no)
            return True if temp is not None else False
        except:
            return False

    @staticmethod
    def validate_email(email):
        email = str(email)

        if not email == "" and not email is None and email.__len__() >= 5:
            try:
                userid, domain = email.split("@")
                host, x = domain.split(".")
                if host and x and userid:
                    return f"{userid}@{domain}"
                else:
                    raise Exception("Invalud emallil")
            except:
                raise InvalidEmailException("Enter a valid emailformat.")
        else:
            raise InvalidEmailException(
                "Empty Email Detected!!"
                if email == "" or email is None
                else "Email should be greater than 5 characters...!"
            )

    @property
    def valid_email(self):
        temp = None
        try:
            temp = self.validate_email(self.email)
            return True if temp is not None else False
        except:
            return False

    @staticmethod
    def validate_username(username):
        return UsernameValidator.validate(username)

    @property
    def all_valid(self):
        return (
            True
            if self.valid_phone_no and self.valid_username and self.valid_email
            else False
        )


class URLValidator:
    class InvalidException(Exception):
        def __init__(self, *args):
            self.message = (
                args[1] or "Invalid url. URL must start with http:// or https://"
            )
            super().__init__(*args)

    @staticmethod
    def validate(*args):
        if len(args) < 1:
            raise ValueError("Url argument is required.")

        else:
            url = URLValidator(args)
            return url.valid_urls

    def __init__(self, *args):
        self.urls = args

    @property
    def valid_urls(self):
        valid_url = []
        urls = self.urls
        for i in urls:
            if str(i).startswith("https://") or str(i).startswith("http://"):

                valid_url.append(str(i))

        self.valid_url = valid_url
        # return valid_url

        return valid_url if not len(self.valid_url) > 0 else None

    def validate(self, url):
        if isinstance(self, str):
            return
