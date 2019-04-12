## Design Document for RJI Project

### Overview
* This is a design document going over what is needed for our use cases to work as planned. It also goes over how our software communicates and the reasons for our design.


### Data Sources
* Valid username and password
* Photos to be uploaded
* Google cloud server (Web UI)
* AWS server (Database)

### Functions
* Log in
* Log out
* Upload image
* Store image info
* Search
* Delete image info

### Source Code
* Image ranking algorithm
* Database
* Web UI

### How Software Communicates
* When uploading images, the user navigates the web ui and chooses the files to upload. The web app then pings the ranking algorithm which then sends back the ranking. The web app then pings the database in order to store the photo id, ranking, tag, etc. Finally the photos and ranking are displayed on the web ui.

### Reasons for Design
* We chose to use a Google cloud and AWS server because they were free and easy to use. We decided it would be beneficial to store data for future use in a database. Our overall design seemed like the most efficent way to solve the problem at hand, and we wanted to utilize the tools around us. This design also fits our groups skills perfectly because we can all contribute to the overall final product.
