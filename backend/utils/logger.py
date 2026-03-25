# backend/utils/logger.py

import datetime

def log(message):
    print(f"[{datetime.datetime.now()}] {message}")