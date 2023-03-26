from flask import Blueprint, render_template, request, flash, session
from flask_login import login_required, current_user
from .models import Book
from . import db
import json
from datetime import date


views = Blueprint('views', __name__)

file = "../Internship assignment/Library_website/static/books.json"
my_books=[]
all_books = []
# Here the file is read and saved in an array of type Book objects, in order to depict them as the School Library's list of Books.
with open(file, 'r') as openfile:
    json_string = openfile.read()
    json_object = json.loads(json_string)

for item in json_object:
    new_book = Book(id=item["id"], name=item["name"], num_of_copies=item["num_of_copies"])
    all_books.append(new_book)
    

    

@views.route('/', methods=['GET', 'POST'])  #Home page before the user adds/removes books from the list
@login_required
def home():
    
    return render_template("home.html", user=current_user, items=all_books)

@views.route('/<int:item_id>', methods=['POST', 'GET'])     #Function that adds books to the user's list, and redirecting him/her to the home page
@login_required                                                     
def add_book(item_id):                                                  
    
    if request.method == "POST":
        for book in all_books:
            if book.id == item_id and already_owned(item_id)==False:
                new_book = Book(id=item_id, name=book.name, date_lent=date.today(), user_id=current_user.id)
                db.session.add(new_book)
                db.session.commit()
                book.num_of_copies-=1
                flash('New Book Added!', category='success')
           
            else:
                flash('You\'ve reached the book limit or book already owned!',category='error')
        
    
    return render_template("home.html", user=current_user, items=all_books)

@views.route('/return-book/<int:item_id>', methods=['POST', 'GET']) #Function that remove books from the user's list, and redirecting him/her to the home page
@login_required
def return_book(item_id):

    if request.method == "POST":
        for book in current_user.books:
            if book.id == item_id:
                if book.user_id == current_user.id:
                    db.session.delete(book)
                    db.session.commit()
                    flash('Book Returned!', category='success')
                for book in all_books:
                    if book.id == item_id:
                        book.num_of_copies+=1
            else:
                flash('Couldn\'t return book!',category='error')
            

    return render_template("home.html", user=current_user, items=all_books)

@login_required
def already_owned(book_id):     #Helper function that uses an array to check if a user has already borrowed the chosen book
    owned = False

    for book in my_books:
        if book.id == book_id:
            owned = True
            break

    return owned 
