from unicodedata import name
from django.urls import path
from .import views

urlpatterns=[
    path('artical',views.articals,name='artical'),
    path('<int:id>/articaltag/',views.artical_tag, name='articaltag'),
    path('saveartical/',views.artical_save,name='saveartical'),
    path('<int:id>articaldelete/',views.artical_delete,name='articaldelete'),
    path('articalfind/<str:cont_tag>',views.artical_find,name='articalfind'),
    
    
]