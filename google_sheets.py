from flask import *
from appdef import app
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GSheet:
  def __init__(self):
    self.scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    self.creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_client_secret.json', self.scope)

  def start(self):
    return(gspread.authorize(self.creds))


#@app.route('/google-sheets')
#def insert_init_sheets():
def insert_into_sheets(tracking, res, sm):

  client = GSheet().start()
  # work book name
  sheet = client.open("Request Ticket Tracker").sheet1
  # row fields
  row = [str(tracking), "N", str(sm)]
  # insert row at the bottom most
  sheet.insert_row(row, len(sheet.get_all_values()) + 1)
  # print(sheet.row_count)
  print(len(sheet.get_all_values()))

  return;
  #return redirect(url_for('main'))

# updates the
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

