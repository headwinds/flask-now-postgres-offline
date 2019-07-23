# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email():
    message = Mail(
        from_email='hakasetenma@gmail.com',
        to_emails='brandonflowers@gmail.com',
        subject='Jasmine bought tarnished Flail',
        html_content='<strong>You have purchased a this shiny Flail</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print("Email status_code: ", response.status_code)
        print("Email body: ", response.body)
        print("Email headers: ", response.headers)
        return response
    except Exception as e:
        print("Email error:", e.message)
        return e
