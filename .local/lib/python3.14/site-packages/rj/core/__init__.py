from rj.exceptions import RJModuleNotInstalledException
try:
    from rj_core import *
except ModuleNotFoundError:
    raise RJModuleNotInstalledException("rj_core")