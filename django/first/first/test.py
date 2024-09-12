# from django.core.mail import send_mail
# from django.conf import settings

# def test_email():
#     try:
#         send_mail(
#             'Test Email Subject',
#             'This is a test email body.',
#             settings.EMAIL_HOST_USER,
#             ['aniketkangude9060@gmail.com'],
#             fail_silently=False,
#         )
#         print("Test email sent successfully.")
#     except Exception as e:
#         print(f"Error sending test email: {str(e)}")
        
# test_email()
import random
import string

# Generate a 6-digit OTP consisting only of numbers
otp = ''.join(random.choices(string.digits, k=6))
print(otp)