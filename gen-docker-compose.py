#!/usr/local/bin/python3
import math
import os
import random
import string

import IPython


def generate_password(pass_len):
    symbols = string.printable.strip()
    return ''.join([symbols[math.floor(int(x) / 256 * len(symbols))] for x in os.urandom(pass_len)])


with open('./docker-compose.yml.template') as f:
    template = f.read()

port = random.randint(30000, 60000)
password = generate_password(16)
password_hash = IPython.lib.passwd(password)

print('Port:', port)
print('Password:')
print(password)


with open('./docker-compose.yml', 'w') as f:
    f.write(template.format(
        port=port,
        password_hash=password_hash
    ))

print('Run')
print('docker-compose up')
