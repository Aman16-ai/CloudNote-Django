from typing import ContextManager
from home.models import NotesInfo
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from home.models import NotesInfo
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        if title != ' ' or title != '':
            note = NotesInfo(title= title,body = body,date = datetime.today(),user=request.user)    
            note.save()
    
        
    return render(request,'index.html')

def about(request):
    notes = NotesInfo.objects.filter(user=request.user)
    context = {'notes':notes}
    return render(request,'allnotes.html',context)

def delete(request,id):
    if request.method == 'POST':
        note = NotesInfo.objects.get(pk=id)
        note.delete()   
        
    return  HttpResponseRedirect('/notes')
    
def update(request,id,title,body):
    print(title)
    print(body)
    # note = NotesInfo.objects.get(pk=id)
    # print(note)
    # title = note.title
    # body = note.body
    # context = {'id':id,'title':title,'body':body}
    context = {'id':id,'title':title,'body':body} 
    return render(request,'update.html',context)
   
   
def edit(request,id):
    if request.method == 'POST':
        newtitle = request.POST['newtitle']
        newbody = request.POST['newbody']
        note = NotesInfo.objects.get(pk=id)
        note.title=newtitle
        note.body = newbody
        note.save()
    return HttpResponseRedirect('/notes')


def back(request):
    return HttpResponseRedirect('/notes')

def search(request):
    if request.method == 'POST':
        title = request.POST['searchnote']
        note = NotesInfo.objects.get(title=title)
        context = {'note':note}
        return render(request,'search.html',context)
        
        
def handleLogin(request):
    return render(request,"Login.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['Username_login']
        password = request.POST['pass_login']
        print(username)
        print(password)
        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Invalid credentials")   
def handleSignup(request):
    return render(request,'Signup.html')

def signupUser(request):
    if request.method == 'POST':
        username = request.POST['Username']
        fisrtname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        email = request.POST['email']
        password = request.POST['pass']
        
        user = User.objects.create_user(username,email,password)
        user.first_name = fisrtname
        user.last_name = lastname
        user.save()
        
        
        
    return HttpResponseRedirect("/")

def logoutUser(request):
    user = logout(request)
    return HttpResponseRedirect("/")