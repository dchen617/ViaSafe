CREATE TABLE countries (
  countryid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  countryname varchar(100) NOT NULL
);

CREATE TABLE `states` (
  stateid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  statename varchar(100) NOT NULL,
  countryid int NOT NULL,
   FOREIGN KEY (countryid) REFERENCES countries(countryid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE cities (
  cityid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  cityname varchar(100) NOT NULL,
  stateid int NOT NULL,
  FOREIGN KEY (stateid) REFERENCES states(stateid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE users (
  userid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username varchar(20),
  passwordhash varchar(1000),
  email varchar(100),
  token varchar(1000)
);

CREATE TABLE locations (
  locationid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title varchar(100) NOT NULL,
  description varchar(1000),
  longitude decimal(12,8),
  latitude decimal(12,8),
  address varchar(100),
  countryid int NOT NULL,
  stateid int NOT NULL,
  cityid int NOT NULL,
  userid int NOT NULL,
  FOREIGN KEY (countryid) REFERENCES countries(countryid) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (stateid) REFERENCES states(stateid) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (cityid) REFERENCES cities(cityid) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (userid) REFERENCES users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
