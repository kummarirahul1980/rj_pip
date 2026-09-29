from copy import deepcopy
import os, smtplib, json, importlib
from functools import wraps
from datetime import datetime
from email.mime.text import MIMEText

from rj.core.exeptions import ImproperlyConfigured
from email.message import EmailMessage
from rj.core.exeptions import RJMailsMIMETypeException
from . import DEFAULT_SERVERS_AVAILABLE

# PREDEFINING THE GLOBAL VARIABLES TO NONE
available_server = []
for i in DEFAULT_SERVERS_AVAILABLE:
    available_server.append(i)

smtp_defaults = deepcopy(DEFAULT_SERVERS_AVAILABLE)
SETTINGS_MODULE = None
settings_module = None
SETTINGS_MODULE_KEYWORD = None
APP_PASSWORD = None
APP_EMAIL = None
MAIL_PORT = None
MAIL_SERVER = None
if True:
    APP_EMAIL = os.environ.get("RJ_MAIL_EMAIL")
    APP_PASSWORD = os.environ.get("RJ_MAIL_PASSWORD")
    MAIL_SERVER_TYPE = os.environ.get("RJ_MAIL_SERVER_TYPE")
    MAIL_PORT = os.environ.get("RJ_MAIL_PORT")
    MAIL_SERVER = os.environ.get("RJ_MAIL_SERVER")


def E_SET_SERVER_AND_PORT(server: str) -> int:
    """
    returns 0 for SUCCESS and 1 or else for unix status of FAILURE
    """
    if not server:
        raise ValueError(" A")
    if smtp_defaults.get(server):
        global MAIL_PORT, MAIL_SERVER
        MAIL_PORT = smtp_defaults[server]["PORT"]
        MAIL_SERVER = smtp_defaults[server]["SERVER"]

    else:
        raise ValueError(
            "SERVER '%s' doesnt exist. Please define port and server manually. "
            % (server)
        )

    return 0 if MAIL_PORT and MAIL_SERVER else 1


if not APP_EMAIL or not APP_PASSWORD or MAIL_SERVER_TYPE:

    SETTINGS_MODULE_KEYWORD = (
        os.environ.get("DEFAULT_PROJECT_SETTINGS_KEYWORD") or "RJ_SETTINGS_CONF_MODULE"
    )
    SETTINGS_MODULE = os.environ.get(SETTINGS_MODULE_KEYWORD)

    error = Exception()
    if not SETTINGS_MODULE:
        message = " Please define the settings credential module RJ_SETTINGS_CONF_MODULE or refer `rjdevelopers mails --help` for more"
        error = ValueError(message)
        raise error

    settings_module = importlib.import_module(SETTINGS_MODULE)
    if not hasattr(settings_module, "RJ_SETTINGS_CONF"):
        raise AttributeError(
            " Please include RJ_SETTINGS_CONF in form of dictionary tree as { 'EMAIL' : { 'APP_PASSWORD' :, 'SENDERS_EMAIL' } }"
        )

    if not isinstance(settings_module.RJ_SETTINGS_CONF, dict):
        raise TypeError("RJ_SETTINGS_CONF must be a dictionary.")

    APP_EMAIL = settings_module.RJ_SETTINGS_CONF["MAILS"]["APP_EMAIL"]
    APP_PASSWORD = settings_module.RJ_SETTINGS_CONF["MAILS"]["APP_PASSWORD"]
    MAIL_SERVER_TYPE = settings_module.RJ_SETTINGS_CONF["MAILS"]["MAIL_SERVER_TYPE"]
    if E_SET_SERVER_AND_PORT(MAIL_SERVER_TYPE):
        raise ImproperlyConfigured
    else:
        print("Success")

print("SErver port : ", MAIL_PORT)
print("Server server", MAIL_SERVER)


def sendmail(receiver_email, text):
    return E_sendmail(APP_EMAIL, APP_PASSWORD)


def E_sendmail(
    sender_email,
    app_password,
    reciever_email,
    message,
    subject,
    return_cls=False,
    mail_type="text",
    html="",
    *args,
    **kwargs,
):
    if not mail_type in ["html", "text"]:
        raise RJMailsMIMETypeException("Mails must be of either html/ or text only.")
    email = EmailMessage()
    email["To"] = reciever_email
    email["From"] = sender_email
    email["subject"] = subject

    email.set_content(message)
    if mail_type == "html":
        email.add_alternative(html, subtype="html")
    with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(email)

    return email if return_cls else "STATUS_SUCCESS"


def E_TEXT_sendmail(
    sender_email, app_password, reciever_email, message, subject, return_cls=False
):
    return E_sendmail(
        sender_email,
        app_password,
        reciever_email,
        message,
        subject,
        return_cls=return_cls,
    )


def E_HTML_sendmail(
    sender_email,
    app_password,
    reciever_email,
    message,
    subject,
    html,
    return_cls=False,
):
    return E_sendmail(
        sender_email,
        app_password,
        reciever_email,
        message,
        subject,
        return_cls=return_cls,
        mail_type="html",
        html=html,
    )


@wraps
def E_THREAD_sendmail(return_thread=False, *args, **kwargs):
    from threading import Thread

    t = Thread(target=sendmail, args=args, kwargs=kwargs)
    t.start()
    return None if not return_thread else t


def sendmail(reciever_mail, text, subject="", return_cls=False):
    return E_sendmail(
        APP_EMAIL, APP_PASSWORD, reciever_mail, text, subject, return_cls=return_cls
    )


def send_template_mail(sender_email, app_password): ...
