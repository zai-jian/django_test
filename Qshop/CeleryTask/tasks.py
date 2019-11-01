from __future__ import  absolute_import
import smtplib
from  email.mime.text import MIMEText

from Qshop.celery import app

@app.task
def add():
    return 3
