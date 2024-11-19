from re import search

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render


from my_app.models import Book
# Create your views here.

def userlistBookView(request):

    books = Book.objects.all()

    paginator=Paginator(books,5)

    page_number = request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)


    return render(request,'user/userdetails.html',{'books':books,'page':page})

def userdetailsView(request,book_id):
    book = Book.objects.get(id=book_id)

    return render(request, 'user/userlist.html', {'book': book})



def userSearch_Book(request):
    query = None
    books=None

    if 'q' in request.GET:

        query=request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    else:
        books=[]

    return render(request,'user/usersearch.html',{'books':books,'query':query})