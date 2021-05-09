from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path("notes/",views.about, name="notes"),
    path('delete/<int:id>',views.delete,name= "delete"),
    path('update/<int:id>/<str:title>/<str:body>',views.update,name = "update"),
    path('edit/<int:id>',views.edit,name = "edit"),
    path('back/',views.back,name="back"),
    path('search/',views.search,name="search"),
    path('login_page',views.handleLogin,name="handleLogin"),
    path('signup_page',views.handleSignup,name="handleSignup"),
    path('signup',views.signupUser,name="signupUser"),
    path('logout',views.logoutUser,name="logoutUser"),
    path('login',views.login,name="login")
]
