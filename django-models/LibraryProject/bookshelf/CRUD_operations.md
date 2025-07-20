- Start Django shahell with:
python manage.py shell

- CRUD Operations 

* Create
python from bookshelf.models import Book 

book = Book.objects.create(
    title="1984", 
    author="George Orwell",        
    publication_year=1949)
    
* Retrieve 
from booshelf.models import  Book 
books = Book.objects.get(title="1984")

* Update
from bookshelf.models import Book 
book = Book.objects.get(title='1984') 
book.title = "Nineteen Eighty-Four"
book.save()

* Delete 
book = Book.objects.get(title='Nineteen Eighty-Four') book.delete()