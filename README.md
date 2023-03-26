## SCHOOL LIBRARY WEB APPLICATION using Python Flask and SQLAlchemy, with user authentication
## Dimitrios Konstantinos Makris
## 26/03/2023


This application is an attempt to build the school’s library portal, so that students can borrow books and return them.
The specifications are:
* There is a list of books depicted in the website, which is imported by a json file included in the folder  /Library_website/static.
* The Library's book list can be modified by adding or removing objects to and from the json file.
* Each student that logs in can borrow up to 3 books, and not more than one copies of each book. 
* Students must return their borrowed books within 30 days.

## REQUIREMENTS
In order to be aple to setup and run this application, it is required to install:
* Python
* flask
* Flask-SQLAlchemy
* flask-login
and perhaps a few other modules the user's computer might be missing.

## RUNNING THE APPLICATION
In order to run the application, the user should navigate into the Libary_website folder and type:
* python3 main.py   , if the user's python version is above 3.0.0 
* python main.py    , otherwise.
After successfully typing this command, the application's server is up and running, and the user can now click on the link that will appear on the screen ( http://127.0.0.1:5000 ), in order to access the website.

## SPECIFICATIONS
* First time accessing the website:
    For the first time the user is accessing the website, it is required to sign up using their credentials.
* Not the first time accessing the website:
    The user can use their credentials that have already been stored in the database, in order to access their account freely.

## PROBLEMS-DETAILS THAT NEED TO BE IMPROVED
Unfortunately, there are a few corrections to be made:
* The date the book was lent is depicted successfully, but there are no notifications in case the time limit is surpassed. 
* When a user has added a book in their list, the other users can't borrow the same book even if the number of copies is > 1, because of a unique constraint. I tried to drop this unique constraint with no success.
