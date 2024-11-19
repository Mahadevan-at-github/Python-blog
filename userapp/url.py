from django.urls import path
from . import views

urlpatterns = [
    path('',views.userlistBookView,name='book-list'),
    path('userdetails/<int:book_id>/',views.userdetailsView,name='userDetails'),
    path('userseach/',views.userSearch_Book,name='userSearch'),

]