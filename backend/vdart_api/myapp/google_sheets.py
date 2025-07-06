import os
import json
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_service():
    creds = Credentials.from_service_account_file(
        os.environ['GOOGLE_CREDENTIALS_FILE'], scopes=SCOPES)
    return build('sheets', 'v4', credentials=creds)

def get_emails_from_sheet():
    sheet_id = os.environ['GOOGLE_SHEET_ID']
    service = get_service()
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id, range="Sheet1!A2:A").execute()
    emails = [row[0] for row in result.get('values', [])]
    return emails

def save_to_sheet(data):
    sheet_id = os.environ['GOOGLE_SHEET_ID']
    service = get_service()
    body = {
        'values': [[data['email'], data['name'], data['phone'], data['department']]]
    }
    service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range="Submissions!A2",
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()
