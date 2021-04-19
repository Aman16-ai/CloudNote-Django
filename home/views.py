from typing import ContextManager
from home.models import NotesInfo
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
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
    pass
        