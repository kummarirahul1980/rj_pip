class RJNotInstalledError(BaseException):
    def __init__(module_name, *args,**kwargs):
        return super()("Module %s not installed. Pleasee refer to docs, and install it to continue using it or try installing by 'pip install rj_%s "%(module_name, module_name))

