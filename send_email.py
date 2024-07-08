import random
import string
from flask_mail import Mail, Message

def generate_verification_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def send_verification_email(email, verification_code):
    msg = Message('Your Verification Code', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    Mail.send(msg)