import os
from dotenv import load_dotenv

load_dotenv()

FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')
SYNC_FOLDER = os.getenv('SYNC_FOLDER')
FIREBASE_BUCKET = os.getenv('FIREBASE_BUCKET')