from .models import Author,Book
from nsapp.serializer import BookSerializer, AuthorSerializer
from rest_framework import generics
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter

# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
    filter_backends=(DjangoFilterBackend,OrderingFilter,SearchFilter)
    filterset_fields=('firstName',)
    ordering=('books__ratings')
    ordering_fields=('firstName',)
    search_fields=('firstName','lastName','books__tite','books__rating','books__author')
    
    #this only work for this class to make this global we make changes to settings.py
    """authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated, DjangoModelPermissions]"""

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
    
class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer