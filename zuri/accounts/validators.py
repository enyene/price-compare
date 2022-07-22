from django.core.validators import EmailValidator

class ValidateEmail(EmailValidator):
    message = 'Enter a valid email address'
    