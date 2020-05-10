import bcrypt


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


user = "Aliuta"
password = hash_password('aliuta')
user = {user: password}
print(user)
print(verify_password("aliuta", '$2b$12$7Vpw8blZy9BZzccQnbXutun9Pj6TEeYBL9ofhx0/qX6HDzMmP7/LO'))
