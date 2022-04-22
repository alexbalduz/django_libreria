from django.conf.urls import url

from . import views


urlpatterns = [
    url('', views.index, name='index'),
    url('books/', views.BookListView.as_view(), name='books'),
]