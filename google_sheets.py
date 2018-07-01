from flask import *
from appdef import app
import gspread
from oauth2client.service_account import ServiceAccountCredentials

<<<<<<< HEAD
def insert_into_sheets(tracking, res, sm):
  # use creds to create a client to interact with the Google Drive API
  scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_client_secret.json', scope)
  client = gspread.authorize(creds)

=======
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
>>>>>>> refs/remotes/origin/master
  # work book name
  sheet = client.open("Request Ticket Tracker").sheet1
  # row fields
  row = [str(tracking), "N", str(sm)]
  # insert row at the bottom most
<<<<<<< HEAD
  sheet.insert_row(row, len(sheet.get_all_values()))
=======
  sheet.insert_row(row, len(sheet.get_all_values()) + 1)
>>>>>>> refs/remotes/origin/master
  # print(sheet.row_count)
  print(len(sheet.get_all_values()))

  return;
<<<<<<< HEAD

#def update_sheets(tracking, res, sm):
=======
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
>>>>>>> refs/remotes/origin/master

