import json

DEFAULT_SERVERS_AVAILABLE = {
    "google": {"SERVER": "smtp.gmail.com", "PORT": "587"},
    "outlook": {"SERVER": "smtp.office365.com", "PORT": "587"},
    "yahoo": {"SERVER": "smtp.mail.yahoo.com", "PORT": "587"},
    "icloud": {"SERVER": "smtp.mail.me.com", "PORT": "587"},
    "zoho": {"SERVER": "smtp.zoho.com", "PORT": "587"},
    "sendgrid": {"SERVER": "smtp.sendgrid.net", "PORT": "587"},
    "mailgun": {"SERVER": "smtp.mailgun.org", "PORT": "587"},
    "brevo": {"SERVER": "smtp-relay.brevo.com", "PORT": "587"},
    "postmark": {"SERVER": "smtp.postmarkapp.com", "PORT": "587"},
    "amazon_ses": {"SERVER": "email-smtp.us-east-1.amazonaws.com", "PORT": "587"},
}

HELP = """
RJ Developers Mail
==================

Configure credentials and send mail.

Environment:
    RJ_MAIL_EMAIL=<email>
    RJ_MAIL_PASSWORD=<app-password>

Or configure:
    RJ_SETTINGS_CONF_MODULE=<settings-module>

Then:
    from rj.mails import sendmail

That's it.
"""


MAILS_HELP_STRING = """

RJ Developers Mail
==================

Send emails using the RJ Mail package.

CONFIGURATION
-------------

The mail module supports two ways to provide credentials.

1. Environment variables

   Set:

       RJ_MAIL_EMAIL=<sender email>
       RJ_MAIL_PASSWORD=<app password>

   These values take priority over the project settings module.

2. Project settings module

   If the environment variables are not available, define:

       RJ_SETTINGS_CONF_MODULE=<python.module.path>

   The module must contain:

       RJ_SETTINGS_CONF = {
           "MAILS": {
               "APP_EMAIL": "...",
               "APP_PASSWORD": "...",
               "MAIL_SERVER_TYPE" : "..."
           }
       }

   The environment variable name used to locate the settings module
   can be customized with:

       DEFAULT_PROJECT_SETTINGS_KEYWORD=<environment variable name>

   If DEFAULT_PROJECT_SETTINGS_KEYWORD is not defined,
   RJ_SETTINGS_CONF_MODULE is used.

EXAMPLE
-------

Environment:

    export RJ_MAIL_EMAIL="sender@example.com"
    export RJ_MAIL_PASSWORD="your-app-password"

Or using a settings module:

    export RJ_SETTINGS_CONF_MODULE="myproject.settings"

    # myproject/settings.py

    RJ_SETTINGS_CONF = {
        "MAILS": {
            "APP_EMAIL": "sender@example.com",
            "APP_PASSWORD": "your-app-password",
            "MAIL_SERVER_TYPE" : "server_type" 
        }
    }
    
    sender_email = ""
    app_password = ""

AVAILABLE SERVERS
-----------------
%s

SECURITY
--------

Use an application password rather than your normal email account
password when the mail provider supports app passwords.

Do not commit credentials or application passwords to source control.

For more information:

    rjdevelopers mails --help

""" % (json.dumps(list(DEFAULT_SERVERS_AVAILABLE), indent=2))


"""

Functions starting with E_ refer to explicit, and can be used by manually providing manual app email, and password, withuot depending on the settings configuration.

"""


def show_help():
    print(MAILS_HELP_STRING)


def help():
    print(HELP)
