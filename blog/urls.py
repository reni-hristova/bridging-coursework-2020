from django.urls    import path
from .              import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

#<int:pk> – integer expected that will transfer to a view as a variable called pk (primary key)
