from rj.exceptions import RJModuleNotInstalledException
try:
    from rj_api import *
except ModuleNotFoundError:
    raise RJModuleNotInstalledException("rj_api")