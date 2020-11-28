from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('single/<int:id>', views.single, name='single'),
    path('login', views.login, name='login'),
    path('author/<str:auth>/post', views.author, name='author'),
    path('category/<str:cat>', views.category, name='category'),
]
