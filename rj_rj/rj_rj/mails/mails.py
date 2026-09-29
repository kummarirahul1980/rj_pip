from copy import deepcopy
import os, smtplib, json, importlib
from functools import wraps
from datetime import datetime
from email.mime.text import MIMEText
from inspect import signature
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
        if server == "manual" and not MAIL_PORT and not MAIL_SERVER:
            raise ImproperlyConfigured(
                "Manual configuration failed. Did you define 'RJ_MAIL_MANUAL_SERVER', 'RJ_MAIL_MANUAL_PORT' ??"
            )
    else:
        raise ValueError(
            "SERVER '%s' doesnt exist. Please define port and server manually. Set env vars, and define server as 'manual' . .."
            % (server)
        )

    return 0 if MAIL_PORT and MAIL_SERVER else 1


def CONFIGURE_MAIL_APP():
    global APP_EMAIL, APP_PASSWORD, MAIL_SERVER_TYPE, MAIL_PORT, MAIL_SERVER
    if not APP_EMAIL or not APP_PASSWORD or MAIL_SERVER_TYPE:
        SETTINGS_MODULE_KEYWORD = (
            os.environ.get("DEFAULT_PROJECT_SETTINGS_KEYWORD")
            or "RJ_SETTINGS_CONF_MODULE"
        )
        SETTINGS_MODULE = os.environ.get(SETTINGS_MODULE_KEYWORD)

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

        APP_EMAIL = settings_module.RJ_SETTINGS_CONF["MAILS"].get("APP_EMAIL")
        APP_PASSWORD = settings_module.RJ_SETTINGS_CONF["MAILS"].get("APP_PASSWORD")
        MAIL_SERVER_TYPE = settings_module.RJ_SETTINGS_CONF["MAILS"]["MAIL_SERVER_TYPE"]
        if E_SET_SERVER_AND_PORT(MAIL_SERVER_TYPE):
            raise ImproperlyConfigured("Please select the server type.")


CONFIGURE_MAIL_APP()


def RUN_APP_PASSWORD_CHECK():
    if not APP_EMAIL or not APP_PASSWORD:
        message = "Email and Passwords for email,  i.e., login credentials for email has not provided. Please configure credentials or refer help for those settings. "
        raise ImproperlyConfigured(message)


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
    html,
    message="",
    subject="",
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


def E_THREAD_sendmail(*args, return_thread=False, **kwargs):
    from threading import Thread

    sig = signature(E_sendmail)
    sig.bind(*args, **kwargs)
    t = Thread(target=E_sendmail, args=args, kwargs=kwargs)
    t.start()
    return None if not return_thread else t


def sendmail(reciever_mail, text, subject="", return_cls=False):

    return E_sendmail(
        APP_EMAIL, APP_PASSWORD, reciever_mail, text, subject, return_cls=return_cls
    )


def send_template_mail(*args, **kwargs):
    args = (APP_EMAIL, APP_PASSWORD, *args)
    sig = signature(E_HTML_sendmail)
    sig.bind(*args, **kwargs)
    return E_HTML_sendmail(*args, **kwargs)


html_TEmplate = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Email</title>
</head>

<body style="margin:0; padding:0; background:#f4f4f4; font-family:Arial,sans-serif;">

    <div style="max-width:600px; margin:40px auto; background:#ffffff;
                padding:30px; border-radius:10px;">

        <h1 style="margin-top:0; color:#222;">
            Hello from Arun Tailors 👋
        </h1>

        <p style="font-size:16px; color:#555;">
            This is a test HTML email sent using my custom
            <strong>Python SMTP abstraction</strong>.
        </p>

        <div style="padding:15px; background:#f0f0f0; border-radius:6px;">
            <strong>SMTP Status:</strong>
            <span style="color:green;"> SUCCESS</span>
        </div>

        <p style="margin-top:25px; color:#555;">
            If you're reading this, the HTML email pipeline worked.
        </p>

        <hr style="border:0; border-top:1px solid #ddd; margin:25px 0;">

        <p style="font-size:12px; color:#999;">
            This is an automated test message.
        </p>

    </div>

</body>
</html>
"""
