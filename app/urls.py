from django.urls import path
from app import views

urlpatterns=[
    path('',views.index,name="index"),
    path('about',views.about, name="about"),
    path('insert',views.insertdata,name="insert"),
    path('update/<int:id>',views.update_data, name="update_data"),
    path('delete/<int:id>',views.delete_data,name="delete_data"),
]