from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me/', views.about, name='about'),
    path('my-projects/', views.my_project, name='project'),
    path('project/fashion-mart-details/',views.fashion_mart_details, name='fashionmart-details'),
    path('project/blog-details/',views.blog_detail, name='blog-detail'),
    path('project/note-details/',views.note_details, name='note-detail'),
    path('contact-me/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/explore-blog/', views.explore_blog, name='explore-blog'),
    path('blog/details/<int:pk>/', views.blog_details, name='blog_details'),
]
