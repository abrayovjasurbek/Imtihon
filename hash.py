import hashlib

def hashed(text:str):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password