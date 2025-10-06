
from math import pow, log2
import sys, io, os, string
import secrets, base64
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

punct = ".:!?/()&#@&_-*%"
keychain_path = "keychain.dat"
delimiter = "Â§"
salt = b'\xb1\xc7\xbb\x04K\xd4\n~uA\xbe\xa4\x1a\xaeV\xe3'

def strength_value(L, N):
    return int(log2(pow(N, L)))

def load_passwords(key):
    if not os.path.isfile(keychain_path):
        save_passwords({}, key)

    with open(keychain_path, 'rb') as f:
        data = f.read()
    data = data.decode()

    db = {}
    for l in io.StringIO(data):
        s = l.strip().split(delimiter)
        db[s[0]] = s[1]
    return db


def save_passwords(db, key):
    data = "\n".join(w + delimiter + p for w, p in db.items())
    data = data.encode()

    with open(keychain_path, 'wb') as f:
        f.write(data)


def is_strong_enough(password, punct=".:;!?/()&#@&_-*%", strength='strong'):
    diverse_enough = False
    big_enough = False
    if     any(c in punct for c in password) \
       and any(c.isupper() for c in password) \
       and any(c.islower() for c in password) \
       and any(c.isdigit() for c in password):
        strong_enough = True
    
    password_size = len(password)
    password_characters = len(string.ascii_letters + string.digits + punct)

    if   strength == 'strong':
        strength_threshold = 100
        if strength_value(password_size, password_characters) >= strength_threshold:
            big_enough = True
    elif strength == 'medium':
        strength_threshold_max = 100
        strength_threshold_min = 80
        if strength_value(password_size, password_characters) < strength_threshold_max \
           and strength_value(password_size, password_characters) >= strength_threshold_min:
            big_enough = True
    elif strength == 'weak':
        strength_threshold_max = 80
        strength_threshold_min = 64
        if strength_value(password_size, password_characters) < strength_threshold_max \
           and strength_value(password_size, password_characters) >= strength_threshold_min:
            big_enough = True
    elif strength == 'very weak':
        strength_threshold = 64
        if strength_value(password_size, password_characters) < strength_threshold:
            big_enough = True
    else:
        strength_threshold = 100
        if strength_value(password_size, password_characters) >= strength_threshold:
            big_enough = True

    return diverse_enough and big_enough


def generate_password(size=13):
    alphabet = string.ascii_letters + string.digits + punct
    password = ""
    while not is_strong_enough(password, punct):
        password = "".join(secrets.choice(alphabet) for _ in range(size))
    return password


def get_password(db, name):
    pass


def set_password(db, name):
    password = generate_password()
    db[name] = password
    print(f'New password for {name} is {password}')

def print_help():
    print("Usage :")
    print('- "python pykey.py get name" to get the password associated to site "name"')
    print('- "python pykey.py set name" to generate (and replace) the password associated to site "name"')
    sys.exit()


def main():
    if __name__ == "__main__":
        print("Pykey - Password manager")

        if len(sys.argv) <= 1:
            print_help()
        elif sys.argv[1] == "get" and len(sys.argv) == 3:
            action = get_password
        elif sys.argv[1] == "set" and len(sys.argv) == 3:
            action = set_password
        else:
            print_help()

        key = b'WNlS4K1hLhAVl8JiYV0Fj8e92EiSEQi5VS4KNGNPQCc='
        db = load_passwords(key)
        action(db, sys.argv[2])
        save_passwords(db, key)


main()