from flask import *
from main import app

import gspread

from json import dumps
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials


class GSheet:
  def __init__(self):
    self.scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    self.creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_client_secret.json', self.scope)

  def start(self):
    return(gspread.authorize(self.creds))


def insert_init_sheets(e_id, u_level, idea, why, tracking_no):
  client = GSheet().start()
  sheet = client.open("Request Ticket Tracker").sheet1

  time = json.dumps(datetime.now(), indent=4, sort_keys=True, default=str)
  row = [time, e_id, u_level, idea, why, tracking_no, False]

  sheet.insert_row(row, len(sheet.get_all_values()) +1)


"""
@app.route('/google-sheets', methods=['GET'])
def insert_init_sheets():
# def insert_into_sheets(tracking, res, sm):

  client = GSheet().start()
  # work book name
  sheet = client.open("Request Ticket Tracker").sheet1
  # row fields
  #row = [str(tracking), "N", str(sm)]
  # insert row at the bottom most

  sheet.insert_row(row, len(sheet.get_all_values()) + 1)
  # print(sheet.row_count)
  print(len(sheet.get_all_values()))
  return redirect(url_for('main'))
  #return;

#def update_sheets(tracking, res, sm):
  #return redirect(url_for('main'))

# updates the values
def update(tracking, value, mode):
  client = GSheet().start()
  sheet = client.open("Request Ticket Tracker").sheet1

  cell_list = sheet.findall(tracking)
  row = cell_list[0].row


  if (mode =="sm"):               # if the mode is sm, then update the field here
    col = cell_list[0].col + 2
  else:                           # else, update the field for resolution
    col = cell_list[0].col + 1

  sheet.update_cell(row, col, value)
"""

