import json
import os

ACCOUNTS_FILE = os.path.join(os.path.dirname(__file__), "accounts.json")

def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as f:
            return json.load(f)
    return []


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)
