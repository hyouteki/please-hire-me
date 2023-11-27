from os.path import exists
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1NcB1bmKRg-j56KUsd7WNHYpkVBx0S7Jkr26LyeJW8HQ"

def get_values():
    credentials = None
    if exists("../creds/token.json"):
        credentials = Credentials.from_authorized_user_file("../creds/token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    "../creds/credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("../creds/token.json", "w") as fd:
            fd.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, 
                                     range="A1:Z6666").execute()
        values = result.get("values", [])
    except HttpError as error:
        print(error)
    return values

def process_values(values):
    weeks = len(values)-2
    status = values[0][2: ]
    users = values[1][2: ]
    print(weeks, users, status)

if __name__ == "__main__":
    process_values(get_values())
