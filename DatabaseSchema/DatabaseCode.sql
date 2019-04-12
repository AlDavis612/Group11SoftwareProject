/* 
Database Schema for Creating 

We only need to create one table to hold the properties of the images 
we ranked, we do not need any other tables as this will be the only 
data we will be collecting

*/

CREATE TABLE Images
(
	imageId			INT PRIMARY KEY;
	rankId 			INT;
	category 		VARCHAR(255);
    imagePath       VARCHAR(255);
	dateTagged 		DATE;

);

CREATE TABLE Ranks 
(
    rankId          INT;
    description     VARCHAR(255);
);

CREATE TABLE Users
(
    userId          INT PRIMARY KEY;
    firstName       VARCHAR(255);
    lastName        VARCHAR(255);
    password        VARCHAR(255);
    role            VARCHAR(255);
);

CREATE TABLE Role
(
    roleId          INT PRIMARY KEY;
    roleName        VARCHAR(255);
);

/*

Database Schema for Inserting Dummy Data

This code is to insert Dummy data into the DB table

*/

INSERT INTO Images
VALUES (12345, 'Mizzou_Football', 123, [path to image], 'Sports');

INSERT INTO Ranks
VALUES ('Picture taken at Mizzou football game');

INSERT INTO Users
VALUES ('Tom', 'Hatherford', 'Hello1234', 'CEO');

INSERT INTO Role
VALUES (123, 'CEO');
