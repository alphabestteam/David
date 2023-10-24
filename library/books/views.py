from django.shortcuts import get_object_or_404
from rest_framework import status

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer


@api_view(['POST'])
def create_new_book(request):
    json_data = request.data
    serializer = BookSerializer(data=json_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def create_author(request):
    json_data = request.data
    serializer = AuthorSerializer(data=json_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PUT'])
def update_book(request):
    json_data = request.data
    book = get_object_or_404(Book, book_id=json_data["book_id"])
    serializer = BookSerializer(book, data=json_data)
    if serializer.is_valid():
        serializer.update(book, json_data)
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def remove_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    book.delete()
    return HttpResponse("Successfully removed book",
                        status=status.HTTP_204_NO_CONTENT)  # No data to return after deletion therefor using HttpResponse


@api_view(['GET'])
def list_all_books(request):
    all_books = Book.objects.all().prefetch_related('author')
    serializer = BookSerializer(all_books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_book_by_title(request, title):
    books = Book.objects.filter(title__icontains=title)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_book_by_author(request):
    author = request.query_params["author"]
    books = Book.objects.filter(author__icontains=author)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_author_name(request):
    json_data = request.data

    book = get_object_or_404(Book, book_id=json_data["book_id"])
    serializer = BookSerializer(book, data=json_data["author"], partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def authors_with_books(request):
    authors = Author.objects.select_related('book')
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def connect_book_to_author(request):
    json_data = request.data
    book = get_object_or_404(Book, book_id=json_data["book_id"])
    author = get_object_or_404(Author, author_id=json_data["author_id"])
    book.author = author
    book.save()
    serializer = BookSerializer(book)
    return Response(serializer.data)
