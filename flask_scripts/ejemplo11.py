from werkzeug.security import generate_password_hash, check_password_hash

password = "password123"
hashed_password = generate_password_hash(password)
print(hashed_password)