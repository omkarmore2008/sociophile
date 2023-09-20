from django.core.mail import send_mail
import random
from .models import User

def send_otp_via_email(email):
    otp = random.randint(100000,999999)
    user = User.objects.filter(email=email)
    for i in user:
        i.otp = otp
        i.save()
    send_mail(
            'OTP verification',
            (f'Your one time password for login is: {otp}'),
            'more.omkar.testing@gmail.com',
            [email],
            fail_silently = False
        )