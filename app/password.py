import hashlib

def encriptacion(password):
    return hashlib.md5(password.encode()).hexdigest()
