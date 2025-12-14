# views.py
from rest_framework import generics
from .models import BookModel
from .serializers import BookSerializer


# 1. Faqat ro'yxat ko'rish
class BookListView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


# 2. Bitta kitobni ko'rish
class BookDetailView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'  # default shu, yozish ixtiyoriy


# 3. Yangi kitob qo'shish
class BookCreateView(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer




# 4. Kitobni yangilash (PUT va PATCH)
class BookUpdateView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


# 5. Kitobni o'chirish
class BookDeleteView(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    lookup_field = 'pk'


# 6. Hammasini bitta joyda: Retrieve + Update + Destroy (eng ko'p ishlatiladi!)
class BookRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


# Bonus: List + Create birlashtirilgan (ko'pincha shunday ishlatiladi)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


from django.shortcuts import render

# Create your views here.
