from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re

class PasswordValidator:
    def __init__(self, min_length=8, max_length=24):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):
        password_pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,24}$'
        if not re.match(password_pattern, password):
            raise ValidationError(
                ('Password must contain one digit from 1 to 9, one lowercase letter, one uppercase letter, one special character, no space, and it must be { self.min_length }-{ self.max_length } characters long'), 
                code='Password to short'
            )
        
    def get_help_text(self):
        return 'Password must contain one digit from 1 to 9, one lowercase letter, one uppercase letter, one special character, no space, and it must be { self.min_length }-{ self.max_length } characters long'

# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext as _


# class MinimumLengthValidator:
#     def __init__(self, min_length=8):
#         self.min_length = min_length

#     def validate(self, password, user=None):
#         if len(password) < self.min_length:
#             raise ValidationError(
#                 _("This password must contain at least %(min_length)d characters."),
#                 code="password_too_short",
#                 params={"min_length": self.min_length},
#             )

#     def get_help_text(self):
#         return _(
#             "Your password must contain at least %(min_length)d characters."
#             % {"min_length": self.min_length}
#         )