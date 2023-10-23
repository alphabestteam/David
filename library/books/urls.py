from django.urls import path, include
from . import views

urlpatterns = [
    path('createBook/', views.create_new_book),
    path('createAuthor/', views.create_author),
    path('updateBook/', views.update_book),
    path('updateAuthorName/', views.update_author_name),
    path('removeBook/<int:book_id>', views.remove_book),
    path('allBooks/', views.list_all_books),
    path('booksByAuthor/', views.search_book_by_author),
    path('connectBookToAuthor/', views.connect_book_to_author),
]
