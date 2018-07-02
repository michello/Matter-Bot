# WMS Request Pipeline
Solution to allow Blue Apron associates to communicate their ideas and needs directly.
At the moment, associates must manually submit ideas for improvements manually
to managers. However, leadership is often busy and packed with deadlines, not
allowing associates a chance to express their ideas. 

![Alt text](images/bot_screenshot.png?raw=true "Title")

## Implementation:
The WMS Request Pipeline aims to address that problem by allowing associates to
submit their ideas through either text messages or a google form. 

![Alt text](images/text_message_screenshot.png?raw=true "Title")

This information is parsed using twilio, then pushed to the appropriate Slack 
channel corrsponding to the employee's information via the python slack client.
From there, an employer can then approve or deny the idea, their choice of which
is then recorded. All the information is stored in a MySQL database and inside 
a spreadsheet file for future reference and resolution.

## How To Run:
- install requirements.txt
- enter python main.py
- app should be running in  localhost:5000

## Built With:
- twilio
- slackclient
- python flask
