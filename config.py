import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    TOKEN = 'feba79e524aad71178fe8bf611458dfb'
    URL = 'https://rekrutacja.teamwsuws.pl'
