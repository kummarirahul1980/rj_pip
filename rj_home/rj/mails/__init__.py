from rj.exceptions import RJModuleNotInstalledException
try:
    from rj_mails import *
except ModuleNotFoundError:
    raise RJModuleNotInstalledException("rj_mails")