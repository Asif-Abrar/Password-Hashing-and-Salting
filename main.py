from hashlib import blake2b
from hmac import compare_digest
import os

username = "user@gmail.com"
print(f"Length of username: {len(username)}")

password = "myPassword".encode()

print(f"Decoded Password: {password.decode()}")
print(f"Encoded Password: {password}")

# --------Static salting and hashing
if len(username) > 16:
    new_username = username[0:16]
    salt = new_username[::-1].encode()
elif len(username) < 16:
    salt = (username[::-1] + username)[0:16].encode()
else:
    salt = username[::-1].encode()

print(f"Salt (Decoded) for hash A: {salt.decode()}")
print(f"Salt for hash A: {salt}")

h = blake2b(digest_size=64, salt=salt)
h.update(password)
a = h.hexdigest()

print(f"Hash for A: {a}")

# --------Random salting and hashing
salt1 = os.urandom(blake2b.SALT_SIZE)

print(f"Salt for hash B: {salt1}")

h1 = blake2b(digest_size=64, salt=salt1)
h1.update(password)
b = h1.hexdigest()

print(f"Hash for B: {b}")

# -------Comparing two hash
print(compare_digest(a, b))
