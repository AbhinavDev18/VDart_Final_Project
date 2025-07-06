from django.core.mail import send_mail
from django.conf import settings
import os


def send_email_with_token(email, token):
    """
    Send an email with a link containing email and token
    """
    domain = os.environ.get('DOMAIN', 'http://localhost:5173')
    link = f"{domain}/form/?email={email}&token={token}"
    subject = "Submit Your Details"
    message = f"Click the link to submit your details: {link}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
