from django.core.exceptions import ValidationError
import re

class PasswordValidator:
    def validate(self, password, user=None):
        password_pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,24}$'
        if not re.match(password_pattern, password):
            raise ValidationError(
                'Password must contain one digit from 1 to 9, one lowercase letter, one uppercase letter, one special character, no space, and it must be 8-24 characters long'
            )
        
    def get_help_text(self):
        return 'Password must contain one digit from 1 to 9, one lowercase letter, one uppercase letter, one special character, no space, and it must be 8-24 characters long'

