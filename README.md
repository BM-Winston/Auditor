## Auditor

### 13/06/2022

## Author

[Winston Musasia]

# Description
This is a web application where a user can view my projects as well as create one.

.


## Live link


## User Story
The user should be able to:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

* 
## Setup and Installation

##### Clone the repository
```bash
git@github.com/BM-Winston/Auditor.git
```
##### Install requirements 
```bash
cd Auditor pip install -r requirements.txt
```
### Install and activate virtual environment
```bash
python3 -m venv virtual - source virtual/bin/activate
```
 ##### Database  
  SetUp your database. Add user and password, host then make migrations. 
 ```bash 
python manage.py makemigrations app
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

ogin