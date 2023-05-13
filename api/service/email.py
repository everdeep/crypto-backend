import os
from flask import render_template
from flask_mail import Message
from app import mail


class EmailService:
    # Send email to user
    def send_email(self, subject, template, recipients, context):
        msg = Message(subject, sender=os.environ.get("MAIL_USERNAME"), recipients=recipients)

        msg.html = render_template(template + ".html", **context)
        mail.send(msg)
