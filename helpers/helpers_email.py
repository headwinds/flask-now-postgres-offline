# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from itsdangerous import URLSafeTimedSerializer


def send_email():
    message = Mail(
        from_email='hakasetenma@gmail.com',
        to_emails='brandonflowers@gmail.com',
        subject='Jasmine bought tarnished Flail',
        html_content='<strong>You have purchased a this shiny Flail</strong>')
    try:
        key = os.environ.get('SENDGRID_API_KEY')
        print("Email key: ", key)
        sg = SendGridAPIClient(key)
        response = sg.send(message)
        print("Email status_code: ", response.status_code)
        print("Email body: ", response.body)
        print("Email headers: ", response.headers)
        return response
    except Exception as e:
        print("Email error:", e)
        return e


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
    return serializer.dumps(email, salt=os.getenv('SECURITY_PASSWORD_SALT'))


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
    try:
        email = serializer.loads(
            token,
            salt=os.getenv('SECURITY_PASSWORD_SALT'),
            max_age=expiration
        )
    except:
        return False
    return email
