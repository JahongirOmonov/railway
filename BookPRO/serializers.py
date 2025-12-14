# serializers.py
from rest_framework import serializers
from .models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id', 'title', 'subtitle', 'author', 'isbn', 'price']
        read_only_fields = ['id']

    def validate(self, data):
        print(">>>>>>>> VALIDATE CALLED <<<<<<<<")
        print("DATA:", data)
        print("TITLE:", data.get("title"))
        print("TYPE:", type(data.get("title")))
        print("<<<<<<<< END VALIDATE <<<<<<<<")
        return data
