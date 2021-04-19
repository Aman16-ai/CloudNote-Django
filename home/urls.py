from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path("notes/",views.about, name="about"),
    path('delete/<int:id>',views.delete,name= "delete"),
    path('update/<int:id>',views.update,name = "update")
    # path("noteSubmit/",views.noteSubmit,name='notesubmit')
]
