class RJModuleNotInstalledException(Exception):
    def __init__(self, module , message = "", *args):
        if message == "" or not message:
           message = (
    "Module '%s' is not installed.\n"
    "Try referring to help, or install it using:\n"
    "    pip install %s"
) % (module, module)
        super().__init__(message)