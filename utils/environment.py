# environment.py

import os

def get_environment():
    """
    Detect or return a testing environment.
    You can set ENV variable in your system or CI/CD like: export ENV=staging
    """
    return os.getenv("ENV", "production")
