from django.urls    import path
from .              import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

#<int:pk> – integer expected that will transfer to a view as a variable called pk (primary key)
