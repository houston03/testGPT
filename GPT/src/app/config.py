import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXTERNAL_SYSTEM_URL = os.getenv('EXTERNAL_SYSTEM_URL')
    EXTERNAL_SYSTEM_LOGIN = os.getenv('EXTERNAL_SYSTEM_LOGIN')
    EXTERNAL_SYSTEM_PASSWORD = os.getenv('EXTERNAL_SYSTEM_PASSWORD')
    CLUB_ID = os.getenv('CLUB_ID')