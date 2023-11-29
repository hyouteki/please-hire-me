from os.path import exists
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import profile_scrapper

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1NcB1bmKRg-j56KUsd7WNHYpkVBx0S7Jkr26LyeJW8HQ"
QUESTIONS_PER_WEEK = 4

def get_sheet():
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
        return service.spreadsheets()
        
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, 
                                     range="A1:Z6666").execute()
        values = result.get("values", [])
    except HttpError as error:
        print(error)
        exit(1)
    return values, sheets

def itoc(index):
    return chr(ord(letter)+index)

def process_sheet(sheets):
    values = sheets.values().get(spreadsheetId=SPREADSHEET_ID, 
            range="A1:Z6666").execute().get("values", [])
    status = values[0][2: ]
    users = values[1][2: ]
    skip = int(values[0][1])
    week_number = skip % QUESTIONS_PER_WEEK 
    print(f"week number = {week_number}")
    alive_users = dict()
    for i in range(len(users)):
        if status[i] == "Alive":
            alive_users[users[i]] = 2+i
    print(f"alive users = {alive_users}")
    this_weeks_questions = dict()
    for i in range(QUESTIONS_PER_WEEK):
        this_weeks_questions[values[2+skip+i][1]] = 2+skip+i
    print(f"this week's questions = {this_weeks_questions}")
    for user in alive_users.keys():
        for ques in profile_scrapper.get_questions(user):
            if ques not in this_weeks_questions:
                continue
            user_index = alive_users[user]
            ques_index = this_weeks_questions[ques]
            if (values[ques_index][user_index] == "Done"):
                continue
            print(f"changing status to done for {user}, {ques}")
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, 
                range=f"{itoc(user_index)}{ques_index+1}", 
                valueInputOption="USER_ENTERED", body={"values": [["Done"]]})

if __name__ == "__main__":
    process_sheet(get_sheet())
