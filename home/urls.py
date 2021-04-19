from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path("notes/",views.about, name="notes"),
    path('delete/<int:id>',views.delete,name= "delete"),
    path('update/<int:id>',views.update,name = "update"),
    path('edit/<int:id>',views.edit,name = "edit"),
    path('back/',views.back,name="back"),
    path('search/',views.search,name="search")
]
