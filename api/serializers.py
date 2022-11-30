
#import framework serializers y los models de los libros
from rest_framework import serializers
from books.models import Book

#
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author','isbn')

