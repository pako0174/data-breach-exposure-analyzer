import requests
import time

def check_email_breaches(email, api_key=None):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "User-Agent": "DataBreachChecker",
        "hibp-api-key": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return []  # No breaches
    else:
        print(f"Error ({response.status_code}) for {email}")
        return None

def check_bulk_emails(email_list, api_key=None):
    results = {}
    for email in email_list:
        print(f"Checking: {email}")
        breaches = check_email_breaches(email, api_key)
        results[email] = breaches
        time.sleep(1.6)  # API rate limit
    return results
