import rj.settings

from rj.settings import *
from rj_core.helpers import jsonify


def formatted_json_string_literal(JSON):
    keys = []
    values = []
    largest_key = ""
    len_largest_key = -1
    if not isinstance(JSON, dict):
        raise TypeError("The argument must be a dict.")
    else:
        for key, value in JSON.items():
            keys.append(key)
            len_key = len(key)
            if len_key > len_largest_key:
                largest_key = key
                len_largest_key = len_key
            values.append(value)

        try:
            print("{\n")
            for key, value in JSON.items():
                len_key = len(key)
                remaining_len = len_largest_key - len_key
                spacing = ""
                for i in range(remaining_len):
                    spacing += " "
                string = key + spacing + "  "
                print("\t%s:  %s" % (string, value))

            print("}")

        except Exception as e:
            print(e)


def chaduvukofirst():
    print("Breakup ainda...?? Poyi Chitti tho kalisi chaduvuko ra poookkaaa!!!!")


def cli_test():

    import sys

    if len(sys.argv) < 2:
        print("No command given")
        exit(1)

    command = sys.argv[1]

    match command:
        case "settings":
            print("__reding__settings__")

        case "read_settings":
            from rj.settings import SETTINGS_JSON_PATH
            import json

            with open(SETTINGS_JSON_PATH, "r") as settings:
                try:
                    settings_dictionary = json.load(settings)
                    formatted_json_string_literal(settings_dictionary)

                except json.JSONDecodeError as e:
                    import sys

                    print(
                        "\033[31mError occurred during handling settings. Improperly configured settings.\033[0m"
                    )
                    print()
                    write_log(e, True)
                    write_log(settings.read())

        case "set_username_validator":
            set_username_validator()
        case "help":
            pass
        case "-h":
            pass
        case "--help":
            help = jsonify(
                settings="reads settings",
                read_settings="reads settings and print out to the terminal",
                set_username_validator="sets username validator regex.",
                read_logs="Prints out the logs written in logs",
                clear_logs="Clears all the log file",
                initialise_settings="Initialises settings, and fixes the errrosr and overwrites settings json, if errors were found.",
            )

            print("avaliable commands:")
            formatted_json_string_literal(help)

        case "read_logs":

            read_logs()

        case "clear_logs":

            settings.clear_logs()

        case "mails":
            from rj.mails import show_help, help

            if sys.argv[2] == "--help":

                show_help()

            else:
                print("Use --help for longer description")
                help()
        case "show_args":
            print(("settings", "read_logs", "read_settings", "clear_logs", "--help"))
        case "initialise_settings":

            initialise_settings()

        case _:
            print("Iinvalid command.")
