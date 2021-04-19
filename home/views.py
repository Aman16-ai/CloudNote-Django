from typing import ContextManager
from home.models import NotesInfo
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from home.models import NotesInfo
from datetime import datetime
# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        if title != ' ' or title != '':
            note = NotesInfo(title= title,body = body,date = datetime.today())    
            note.save()
    
        
    return render(request,'index.html')

def about(request):
    notes = NotesInfo.objects.all()
    context = {'notes':notes}
    return render(request,'allnotes.html',context)

def delete(request,id):
    if request.method == 'POST':
        note = NotesInfo.objects.get(pk=id)
        note.delete()   
        
    return  HttpResponseRedirect('/notes')
    
def update(request,id):
    context = {'id':id}
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
        