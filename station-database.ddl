
CREATE TABLE review (
  ID              SERIAL NOT NULL, 
  bericht         varchar(140) NOT NULL, 
  datum_ingedient timestamp NOT NULL, 
  datum_moderatie timestamp NOT NULL, 
  naam            varchar(255) NOT NULL, 
  keuring         bool NOT NULL, 
  Moderatoremail  varchar(255) NOT NULL, 
  station         varchar(50) NOT NULL, 
  PRIMARY KEY (ID));

CREATE TABLE Moderator (
  email varchar(255) NOT NULL, 
  naam  varchar(255) NOT NULL, 
  PRIMARY KEY (email));

CREATE TABLE station_service (
  station_city  varchar(50) NOT NULL, 
  country       varchar(2) NOT NULL, 
  ov_bike       bool NOT NULL, 
  elevator      bool NOT NULL, 
  toilet        bool NOT NULL, 
  park_and_ride bool NOT NULL, 
  PRIMARY KEY (station_city));

ALTER TABLE review ADD CONSTRAINT FKreviewmoderator FOREIGN KEY (Moderatoremail) REFERENCES Moderator (email);

ALTER TABLE review ADD CONSTRAINT FKreviewstation FOREIGN KEY (station) REFERENCES station_service (station_city);

INSERT INTO station_service (
-- station_id, station_code, station_name,
station_city, country, ov_bike, elevator, toilet, park_and_ride)
VALUES
('Arnhem', 'NL', true, false, true, false),
('Almere', 'NL', false, true, false, true),
('Amersfoort', 'NL', true, false, true, false),
('Almelo', 'NL', false, true, false, true),
('Alkmaar', 'NL', true, false, true, false),
('Apeldoorn', 'NL', false, true, false, true),
('Assen', 'NL', true, false, true, false),
('Amsterdam', 'NL', false, true, false, true),
('Boxtel', 'NL', true, false, true, false),
('Breda', 'NL', false, true, false, true),
('Dordrecht', 'NL', true, false, true, false),
('Delft', 'NL', false, true, false, true),
('Deventer', 'NL', true, false, true, false),
('Enschede', 'NL', false, true, false, true),
('Gouda', 'NL', true, false, true, false),
('Groningen', 'NL', false, true, false, true),
('Den Haag', 'NL', true, false, true, false),
('Hengelo', 'NL', false, true, false, true),
('Haarlem', 'NL', true, false, true, false),
('Helmond', 'NL', false, true, false, true),
('Hoorn', 'NL', true, false, true, false),
('Heerlen', 'NL', false, true, false, true),
('Den Bosch', 'NL', true, false, true, false),
('Hilversum', 'NL', false, true, false, true),
('Leiden', 'NL', true, false, true, false),
('Lelystad', 'NL', false, true, false, true),
('Leeuwarden', 'NL', true, false, true, false),
('Maastricht', 'NL', false, true, false, true),
('Nijmegen', 'NL', true, false, true, false),
('Oss', 'NL', false, true, false, true),
('Roermond', 'NL', true, false, true, false),
('Roosendaal', 'NL', false, true, false, true),
('Sittard', 'NL', true, false, true, false),
('Tilburg', 'NL', false, true, false, true),
('Utrecht', 'NL', true, false, true, false),
('Venlo', 'NL', false, true, false, true),
('Vlissingen', 'NL', true, false, true, false),
('Zaandam', 'NL', false, true, false, true),
('Zwolle', 'NL', true, false, true, false),
('Zutphen', 'NL', false, true, false, true);
