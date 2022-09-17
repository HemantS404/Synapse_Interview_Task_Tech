from email import message
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    f = requests.get('https://dog.ceo/api/breeds/list/all')
    return render(request, 'task1/index.html', f.json())

def s_r(request):
    j = request.GET['breed']
    f = requests.get('https://dog.ceo/api/breed/{}/list'.format(j)).json()
    g = requests.get('https://dog.ceo/api/breed/{}/images/random'.format(j)).json()
    if f == {'message': [], 'status': 'success'}:
        return render(request, 'task1/NotFound.html', {'sub':f, 'img': g})
    return render(request, 'task1/sub_breed.html', {'sub':f, 'img': g})