

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
