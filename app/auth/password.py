import bcrypt

def create_hash_password(password:str):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

def verify_password(password:str, hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8",), hashed_password.encode("utf-8")
    )
