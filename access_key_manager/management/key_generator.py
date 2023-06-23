from secrets import token_urlsafe
# import random as rd
# import string
def generate_key(length):
    # random 32 character key length
    # return ''.join(rd.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32))
    return token_urlsafe(length)

# generate_access_key = generate_key()
generate_access_key = generate_key(32)
# print(key)