# urls.py (masalan: books/urls.py)
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookRUDView,
    BookListCreateView,
)

urlpatterns = [
    # Variant 1: Alohida-alohida
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Variant 2: Retrieve + Update + Delete bitta URL da (tavsiya etiladi!)
    path('books/<int:pk>/rud/', BookRUDView.as_view(), name='book-rud'),

    # Variant 3: List va Create bitta URL da (eng ko'p ishlatiladigan)
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookRUDView.as_view(), name='book-detail-rud'),
]