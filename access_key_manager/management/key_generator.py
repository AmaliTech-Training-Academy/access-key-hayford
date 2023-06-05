import secrets

def generate_key(length):
    # random 32 character key length
    return secrets.token_hex(length)

generate_access_key = generate_key()