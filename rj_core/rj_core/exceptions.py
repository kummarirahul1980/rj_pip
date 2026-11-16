class BaseException(Exception):
    def __init__(self, message="Value is required."):
        self.message = f" {message}."
        super().__init__(message)


class PhoneNumberException(Exception):
    message = "Invalid Phone number formats."

    def __init__(self, message="Invalid Phone number formats."):
        super().__init__(self.message)


class InvalidCountryCodeException(Exception):
    def __init__(self, message="Invalid country code format."):
        self.message = f"InvalidPhoneNumberException : {message}."
        super().__init__(self.message)


class InvalidPhoneNumberException(Exception):
    def __init__(self, message="Phone number should contain atleast 10 digits."):
        self.message = f"{message}."
        super().__init__(self.message)


class InvalidEmailException(Exception):
    def __init__(self, message="Email format is invalid."):
        self.message = f"{message}."
        super().__init__(self.message)


class UsernameException(BaseException):
    def __init__(self, message="Invalid Username format."):
        self.message = f"{message}"
        super().__init__(self.message)


class ValidatePhoneNumber(Exception):

    @staticmethod
    def validate_phone(phone):
        phone = str(phone)
        country_code = phone[:-10]
        if not phone.startswith("+") and len(country_code) < 2:
            error_message = f"{phone} : Invalid countrycode country code is empty."
            raise PhoneNumberException(error_message)

        if len(phone) > 15 or len(phone) < 10:
            PhoneNumberIsValid = True
            for i in phone:
                if int(i) in range(0, 9):
                    pass
                else:
                    PhoneNumberIsValid = False
                    raise PhoneNumberException(
                        f"{phone} : Phone Number should contain only Digits (0-9)."
                    )
            raise PhoneNumberException(
                f"{phone} : Phone number should be exactly 10 digits."
            )
        else:
            phone_number = phone[-10:]
        return {"phone_number": phone_number, "country_code": country_code}

    def __call__(self, phone):
        return self.validate_phone(phone)


class MissingFieldError(ValueError):
    def __init__(self, field="", *args):
        self.message = f"The filed -- {field if not field == "" or field is not None else "__NOT_MENTIONED__"} -- is missing."
        super().__init__(self.message)


class IncompleteWritingError(BaseException):
    def __init__(self, *args):
        super().__init__("Error... The code is marked as incompete")


class ImproperlyConfigured(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class RJMailsMIMETypeException(Exception): ...
