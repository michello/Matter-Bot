from flask import *
from appdef import app
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def insert_into_sheets(tracking, res, sm):
  # use creds to create a client to interact with the Google Drive API
  scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_client_secret.json', scope)
  client = gspread.authorize(creds)

  # work book name
  sheet = client.open("Request Ticket Tracker").sheet1
  # row fields
  row = [str(tracking), "N", str(sm)]
  # insert row at the bottom most
  sheet.insert_row(row, len(sheet.get_all_values()))
  # print(sheet.row_count)
  print(len(sheet.get_all_values()))

  return;

#def update_sheets(tracking, res, sm):

