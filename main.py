import pandas as pd
from src.hibp_lookup import check_bulk_emails

API_KEY = "your_api_key_here"

def main():
    df = pd.read_csv("data/emails.csv")
    email_list = df["email"].dropna().tolist()
    results = check_bulk_emails(email_list, API_KEY)

    for email, breaches in results.items():
        if breaches:
            print(f"{email} FOUND in {len(breaches)} breaches.")
        else:
            print(f"{email} OK.")

if __name__ == "__main__":
    main()
