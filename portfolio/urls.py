from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me/', views.about, name='about'),
    path('my-projects/', views.my_project, name='project'),
    path('project/fashion-mart-details/',views.fashion_mart_details, name='fashionmart-details'),
    path('project/blog-details/',views.blog_details, name='blog-detail'),
    path('project/note-details/',views.note_details, name='note-detail'),
    path('contact-me/', views.contact, name='contact'),
]
