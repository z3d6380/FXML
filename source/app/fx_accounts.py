#!/usr/bin/env python

# File: fx_accounts.py
# Written By: Luis Moraguez
# Description: Contains all settings and methods to work with accounts through OANDA forex api (Can be configured to work with other APIs)

# IMPORTS
import json
import os
from security import safe_requests

# FOREX API SETTINGS
if os.getenv("FLASK_ENV") == "production":
    FX_BASE_URL = os.getenv("FX_BASE_URL")
    FX_TOKEN = os.getenv("FX_TOKEN")
    FX_ACCOUNT = os.getenv("FX_ACCOUNT")
    FX_ACCOUNT_ID = os.getenv("FX_ACCOUNT_ID")
else:
    FX_BASE_URL = os.getenv("FX_DEV_BASE_URL")
    FX_TOKEN = os.getenv("FX_DEV_TOKEN")
    FX_ACCOUNT = os.getenv("FX_DEV_ACCOUNT")
    FX_ACCOUNT_ID = os.getenv("FX_DEV_ACCOUNT_ID")

headers = {'Authorization': 'Bearer ' + FX_TOKEN}

get_params = {
    'Content-Type': 'application/json',
    'method': 'GET',
    'headers': headers
}

# METHODS
def get_account(id):
    url = '{0}accounts/{1}'.format(FX_BASE_URL, id)
    response = safe_requests.get(url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_accounts():
    url = '{0}accounts'.format(FX_BASE_URL)
    response = safe_requests.get(url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
