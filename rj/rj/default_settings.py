import os

default_json = {
    "env_file": os.environ.get("HOME/.rjdevelopers"),
    "regex": {
        "username_regex": "^[a-zA-Z0-9._]+$",
        "email_username_regex": "^[a-zA-Z0-9._]+$",
        "email_domain_regex": "^[a-zA-Z.]+$",
    },
    "api": {"API_SIGNATURE": {"start": "Rj-Api", "end": "RJ-end"}},
    "settings": {
        "RJ_SETTINGS_HOME": os.environ.get("HOME"),
        "DEFAULT_HOME": os.environ.get("HOME"),
    },
}
