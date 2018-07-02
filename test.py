from appdef import app, conn

cursor_three = conn.cursor()
reviewer_query = "CREATE TABLE Ticket ( \
  ticket_id INT NOT NULL AUTO_INCREMENT, \
  idea TEXT, \
  why TEXT, \
  urgency INT, \
  resolution VARCHAR(255), \
  person_in_charge INT DEFAULT 0, \
  date_created DATETIME, \
  PRIMARY KEY (ticket_id), \
  FOREIGN KEY (person_in_charge) REFERENCES Employee(EMPLID) \
);"
cursor_three.execute(reviewer_query)
#reviewer = cursor_three.fetchall()
cursor_three.commit()
cursor_three.close()
