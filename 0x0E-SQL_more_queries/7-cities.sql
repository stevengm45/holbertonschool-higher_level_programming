-- creates the database hbtn_0d_usa and the table cities on your MySQL server

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbt_0d_usa.cities(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL FOREIGN KEY, name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
