CREATE DATABASE biodb
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;



CREATE TABLE morth(
    "id"                  integer PRIMARY KEY,
    "Name"                varchar(200),
    "Date"                date,
    "PolygonId"           integer,
    "00"                  numeric,
    "01"                  numeric,
    "10"                  numeric,
    "11"                  numeric,
    "Kingdom"             varchar(200),
    "Class"               varchar(200),
    "Family"              varchar(200),
    "Taxa"                varchar(200)
);


CREATE TABLE otherinsect(
    "id"                  integer PRIMARY KEY,
    "Name"                varchar(200),
    "Date"                date,
    "PolygonId"           integer,
    "00"                  numeric,
    "01"                  numeric,
    "10"                  numeric,
    "11"                  numeric,
    "Kingdom"             varchar(200),
    "Class"               varchar(200),
    "Family"              varchar(200),
    "Taxa"                varchar(200)
);

CREATE TABLE butterfly(
    "id"                  integer PRIMARY KEY,
    "Name"                varchar(200),
    "Date"                date,
    "PolygonId"           integer,
    "00"                  numeric,
    "01"                  numeric,
    "10"                  numeric,
    "11"                  numeric,
    "Kingdom"             varchar(200),
    "Class"               varchar(200),
    "Family"              varchar(200),
    "Taxa"                varchar(200)
);

CREATE TABLE spider(
    "id"                  integer PRIMARY KEY,
    "Name"                varchar(200),
    "Date"                date,
    "PolygonId"           integer,
    "00"                  numeric,
    "01"                  numeric,
    "10"                  numeric,
    "11"                  numeric,
    "Kingdom"             varchar(200),   
    "Class"               varchar(200), 
    "Family"              varchar(200), 
    "Taxa"                varchar(200)
); 


CREATE TABLE odonata(
    "id"                  integer PRIMARY KEY,
    "Name"                varchar(200),
    "Date"                date,
    "PolygonId"           integer,
    "00"                  numeric,
    "01"                  numeric,
    "10"                  numeric,
    "11"                  numeric,
    "Kingdom"             varchar(200),
    "Class"               varchar(200),
    "Family"              varchar(200),
    "Taxa"                varchar(200)
);

CREATE TABLE coleoptera(
    "id"                  integer PRIMARY KEY,
    "Name"                varchar(200),
    "Date"                date,
    "PolygonId"           integer,
    "00"                  numeric,
    "01"                  numeric,
    "10"                  numeric,
    "11"                  numeric,
    "Kingdom"             varchar(200),
    "Class"               varchar(200),
    "Family"              varchar(200),
    "Taxa"                varchar(200)
);



COPY morth("id","Name","Date","PolygonId","00","01","10","11","Kingdom","Class","Family","Taxa") FROM '/db/morth.csv' DELIMITER ',' CSV HEADER;
COPY butterfly("id","Name","Date","PolygonId","00","01","10","11","Kingdom","Class","Family","Taxa") FROM '/db/butterfly.csv' DELIMITER ',' CSV HEADER;
COPY spider("id","Name","Date","PolygonId","00","01","10","11","Kingdom","Class","Family","Taxa") FROM '/db/spider.csv' DELIMITER ',' CSV HEADER;
COPY odonata("id","Name","Date","PolygonId","00","01","10","11","Kingdom","Class","Family","Taxa") FROM '/db/odonata.csv' DELIMITER ',' CSV HEADER;
COPY coleoptera("id","Name","Date","PolygonId","00","01","10","11","Kingdom","Class","Family","Taxa") FROM '/db/coleoptera.csv' DELIMITER ',' CSV HEADER;
