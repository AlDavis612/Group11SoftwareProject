/* 
Database Schema for Creating 

We only need to create one table to hold the properties of the images 
we ranked, we do not need any other tables as this will be the only 
data we will be collecting

*/

CREATE TABLE ranked_images
(
	imageId			INTEGER PRIMARY KEY;
	rank 			INTEGER;
	tags 			CHAR;
	dateTagged 		DATE;

);

/*

Database Schema for Inserting Dummy Data

This code is to insert Dummy data into the DB table

*/

INSERT INTO ranked_images
VALUES (12345, 5, 'Sports');

INSERT INTO ranked_images
VALUES (12346, 2, 'Community');

INSERT INTO ranked_images
VALUES (12347, 1, 'Nature');

INSERT INTO ranked_images
VALUES (12348, 3, 'Campus');