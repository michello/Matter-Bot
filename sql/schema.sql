CREATE TABLE Person(
  p_id INT AUTO_INCREMENT,
  phone_number INT,
  first_name VARCHAR (50),
  last_name VARCHAR (50),
  PRIMARY KEY (t_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Ticket(
  t_id INT AUTO_INCREMENT,
  p_id INT,
  content VARCHAR (250),
  dept_type VARCHAR(50),
  FOREIGN KEY (p_id) REFERENCES Person (p_id)
  PRIMARY KEY (t_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

