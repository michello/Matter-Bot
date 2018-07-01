CREATE TABLE Employee (
  EMPLID INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100),
  employee_name VARCHAR(255),
  department VARCHAR(255),
  groupname VARCHAR(255),
  PRIMARY KEY(EMPLID)
);

CREATE TABLE Ticket (
  ticket_id INT NOT NULL AUTO_INCREMENT,
  idea TEXT,
  urgency INT,
  resolution VARCHAR(255),
  in_charge INT NOT NULL ,
  date_created DATETIME,
  PRIMARY KEY (ticket_id),
  FOREIGN KEY (in_charge) REFERENCES Employee(EMPLID)
);
