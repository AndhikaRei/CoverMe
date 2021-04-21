import bcrypt

def encrypt_password(password):
    encode_password = str.encode(password)
    
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encode_password, salt)

    return hashed.decode("utf-8")

def check_password(password, hashed):
    encode_password = str.encode(password)
    encode_hashed = str.encode(hashed)
    
    if bcrypt.checkpw(encode_password, encode_hashed):
        return True
    else:
        return False