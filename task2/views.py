from django.shortcuts import render
from task2.models import EventManagment
from django.http import HttpResponse
from task2.models import EventManagment

def index(request):
    return render(request, 'task2/index.html')

def action(request):
    response = request.GET['operation']
    if response == 'Display':
        data = EventManagment.objects.all()
        return render(request, 'task2/display.html',{'data': data})
    elif response == 'Create':
        return render(request, 'task2/create_form.html')
    elif response == 'Delete':
        data = EventManagment.objects.all()
        return render(request, 'task2/delete.html',{'data': data})
    elif response == 'Update':
        data = EventManagment.objects.all()
        return render(request, 'task2/update.html',{'data': data})
    else:
        return render(request, 'task2/index.html')

def create(request):
    evename = request.GET['name']
    dateTime = request.GET['date'] +','+request.GET['time']
    audience = request.GET['audience']
    email = request.GET['email']
    i = EventManagment(
        name = evename,
        date_of_event = dateTime,
        event_complete = False,
        No_of_audience = audience,
        Email_of_organizer = email
    )
    i.save()
    return HttpResponse("<h1>DATA STORED SCCESSFULLY !!</h1>")

def delete(request):
    id_ = request.GET['row']
    if id_ == '':
        data = EventManagment.objects.all()
        return render(request, 'task2/delete.html',{'data': data})
    else:
        EventManagment.objects.filter(id = id_).delete()
        return HttpResponse("<h1>DATA DELETED SCCESSFULLY !!</h1>")

def update(request):
    id_ = request.GET['row']
    if id_ == '':
        data = EventManagment.objects.all()
        return render(request, 'task2/update.html',{'data': data})
    else:
        name = request.GET['name']
        date = request.GET['date']
        time = request.GET['time']
        audience = request.GET['audience']
        email = request.GET['email']
        try:
            status = bool(request.GET['status'])
        except:
            status = False
        Data = EventManagment.objects.get(id = id_)
        if name != '':
            Data.name = name  
        if date != '':
            Data.date_of_event = date+','+time
        if time != '':
            Data.event_complete = status
        if audience != '':
            Data.No_of_audience = audience
        if email != '': 
            Data.Email_of_organizer = email
        Data.save()
        return HttpResponse("<h1>Data Saved Successfully !!</h1>")

