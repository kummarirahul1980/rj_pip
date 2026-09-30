from rj.exceptions import RJModuleNotInstalledException
try:
    from rj_mails import mails
except ModuleNotFoundError:
    raise RJModuleNotInstalledException("rj_mails")