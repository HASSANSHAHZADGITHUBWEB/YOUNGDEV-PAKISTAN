from django.shortcuts import render,HttpResponse,render,redirect
from firstapp import models
def login(request):
    if request.method == "POST":
        bookname = request.POST.get('bookname')
        
        # Fetch the book details from the Book model
        book_data = models.Book.objects.filter(bname=bookname).values()
        book_data = list(book_data)  # Convert QuerySet to list
        
        if book_data:  # If a book is found
            # Fetch the slot details from the BookPlace model
            book_id = book_data[0]['bookid']  # Get book ID from the first record
            slot_data = models.BookPlace.objects.filter(bookid=book_id).values('slot')
            slot_data = list(slot_data)  # Convert QuerySet to list
            
            # Add slot data to the existing book data in a single list
            combined_data = {
                'bookid': book_data[0]['bookid'],
                'bname': book_data[0]['bname'],
                'bookstatus': book_data[0]['bookstatus'],
                'bisbn': book_data[0]['bisbn'],
                'slot': [slot['slot'] for slot in slot_data]  # Store slot data in a list
            }

            print(combined_data)
            return render(request, 'login.html', context={'list': [combined_data]})
        
    return render(request, 'login.html')

# Create your views here.
