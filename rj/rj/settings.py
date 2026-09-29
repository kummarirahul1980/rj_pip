from rj.core.exeptions import IncompleteWritingError
from pathlib import Path
from os import path, environ
from rj import default_settings
import os, json
from rj.default_settings import default_json

RJ_SETTINGS_HOME_ENV_VAR = default_settings.default_json.get("settings").get(
    "RJ_SETTINGS_HOME"
)
DEFAULT_HOME = default_settings.default_json.get("settings").get("DEFAULT_HOME")
HOME_DIR = environ.get(RJ_SETTINGS_HOME_ENV_VAR, DEFAULT_HOME)


class HomeDirNotSetException(Exception):
    pass


__base_dir__ = Path(HOME_DIR).resolve().parent
(__base_dir__ / ".rjdevelopers").mkdir(parents=True, exist_ok=True)
__settings_json_path__ = path.join(__base_dir__, ".rjdevelopers/rj_settings.json")

__settings_json__ = Path(__settings_json_path__)
__settings_json__.touch(exist_ok=True)


FILE = Path(__file__)
BASE_DIR = FILE.resolve().parent
# SETTINGS_JSON=Path(BASE_DIR).resolve().join("rj_settings.json")

SETTINGS_JSON_PATH = os.path.join(__base_dir__, "rj_settings.json")

from rj.default_settings import default_json


def write_log(log=None, error=None):
    log_path = os.path.join(__base_dir__, "rj_logs.txt")
    Path(log_path).touch(exist_ok=True)
    with open(log_path, "a") as logs:
        from datetime import datetime

        log_to_be_written = f" \n\n[ rj logs ] [{datetime.now()}] : \n{log}"
        if error:
            log_to_be_written = f"\nError -- {error}\n {log_to_be_written}"
        logs.write(log_to_be_written)
        return log_to_be_written


def read_logs():
    log_path = os.path.join(__base_dir__, "rj_logs.txt")
    Path(log_path).touch(exist_ok=True)
    with open(log_path, "r") as logs:
        logs.seek(0)
        write_log(logs.read())


def clear_logs():
    log_path = os.path.join(__base_dir__, "rj_logs.txt")
    Path(log_path).touch(exist_ok=True)
    with open(log_path, "w") as logs:
        logs.write("")


def write_settings_json(*args, **kwargs):
    from rj.default_settings import default_json

    write_log("Settings json  Initialising...")
    write_log(f"default json :  {default_json}")
    __settings_json__.touch(exist_ok=True)
    with open(__settings_json_path__, "w") as settings:
        settings.seek(0)

        Path(__settings_json_path__).touch(exist_ok=True)
        write_log("settings json default", write_log(default_json))
        x = json.dump(default_json, settings)

        settings.seek(0)
    with open(__settings_json_path__, "r") as settings:
        settings.seek(0)
        returnx = settings.read()

        return returnx


def write_settings(**kwargs):
    settings_dict = {}

    with open(__settings_json_path__, "r") as settings:
        settings.seek(0)
        setting_string = settings.read()
        settings_dict = json.loads(setting_string)

    with open(__settings_json_path__, "w") as settings:
        settings.seek(0)
        settings_dict.update(kwargs)
        settings.write(json.dumps(settings_dict))


def read_settings():
    with open(__settings_json_path__, "r") as settings:
        settings.seek(0)
        setting_string = settings.read()
        settings_dict = json.loads(setting_string)
        return settings_dict


def initialise_settings():

    write_log("settings are initialising....")
    if not __settings_json__.exists():
        write_log("Settings.json doesnt exist ")
        write_settings_json()

    if __settings_json__.exists():
        with open(__settings_json_path__, "r") as settings_json:
            settings_json.seek(0)
            if settings_json.read() == "":
                write_settings_json()
                settings_json.seek(0)

                write_log("Written sett>ngs.json")
            else:
                write_log("Settings json is not empty 🫗 ")

            try:
                settings_json.seek(0)
                read_settings_json = settings_json.read()
                DEFAULT_SETTINGS_DICT = json.loads(read_settings_json)
                write_log("JSONREAD")
                write_log(DEFAULT_SETTINGS_DICT)
                R = DEFAULT_SETTINGS_DICT.get("regex")
                if not (
                    R.get("username_regex")
                    and R.get("email_domain_regex")
                    and R.get("email_username_regex")
                ):
                    write_log(DEFAULT_SETTINGS_DICT.get("username_regex"))
                    write_log(DEFAULT_SETTINGS_DICT.get("email_domain_regex"))
                    write_log(DEFAULT_SETTINGS_DICT.get("email_username_regex"))

                    raise json.JSONDecodeError("", '{"key" : "value"}', 0)
                write_log("Return DEFAULT_SETTINGS_DICT success")
                return DEFAULT_SETTINGS_DICT
            except json.JSONDecodeError as e:
                write_log()
                write_log("Decode error : settings json is of invalid format.", True)
                settings_json.seek(0)

                write_log("Read settings json from decode errrir")
                write_log(e)
                write_log(settings_json.read())
                write_log("Return DEFAULT_SETTINGS_DICT json decode error")
                write_log(e)

                write_log(settings_json.read())

                return write_settings_json()
            except Exception as e:
                write_log(e)
                import sys

                sys.exit(1)
                write_log(e, True)
                write_log("Return DEFAULT_SETTINGS_DICT jErrri")
                write_settings_json()
                write_log("Read settings")

                write_log(settings_json.read())
                return initialise_settings()


def set_username_validator(validator=None):
    if validator:
        with open(__settings_json_path__, "r") as settings:
            settings.seek(0)
            try:

                VALIDATORS = json.loads(settings.read())
                VALIDATORS["username_regex"] = validator
                return VALIDATORS["username_regex"]
            except Exception as e:
                write_log(e)


DEFAULT_SETTINGS_DICT = default_json

API_SIGNATURE = DEFAULT_SETTINGS_DICT["api"]["API_SIGNATURE"]


def write_app_log(date, level):
    import os

    LOG_FILE = "application.log"
    import datetime

    now = datetime.datetime.now()
    data = f"""[{now}] [{level or "undefined_level"}]
{data}

"""
    with open(LOG_FILE, "a") as logfile:
        logfile.write(data)
        write_log("Log written at: ", os.getcwd() / LOG_FILE)


__default_validators__ = {}
if not HOME_DIR:
    raise HomeDirNotSetException(
        "ENV VAR : " + RJ_SETTINGS_HOME_ENV_VAR + " Not set. please export it."
    )

elif HOME_DIR:
    try:
        __default_validators__ = initialise_settings()

    except PermissionError:
        import traceback

        write_log("==============================")
        write_log(
            "permission required to write settings to use validators or try without using validators......"
        )
        write_log("=============================")
        write_log("Please read the docs for further details...")
        traceback.write_log_exc()


class Settings: ...


class attrHelpers: ...


class KeyValuePair:
    def __init__(self, key, value):
        self.key = value


x = read_settings()


def set_class_attr(dictx: dict, cls):
    raise IncompleteWritingError
    for key, value in dictx.keys():

        if isinstance(value, dict):
            set_class_attr(value, key)
