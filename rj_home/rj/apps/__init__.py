from rj.exceptions import RJModuleNotInstalledException
try:
    from rj_apps import *
except ModuleNotFoundError:
    raise RJModuleNotInstalledException("rj_apps")