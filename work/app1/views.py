'''Views file for app1'''

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    '''Returns main page'''
    return render(request, 'index.html')

def about(request):
    '''Returns about page'''
    return render(request, 'about.html')

def contact(request):
    '''Returns contact page'''
    return render(request, 'contact.html')

def data_list(request):
    '''Returns data list page'''
    data = ['Apple', 'Banana', 'Corn', 'Veggies', 'Fruits']
    return render(request, 'data.html', {'data': data})

def render_data(request):
    '''Returns data list page'''
    data = [
        {'id': 1, 'name': 'John Doe', 'age': 28, 'city': 'Moscow'},
        {'id': 2, 'name': 'Jane Smith', 'age': 34, 'city': 'Volgograd'},
        {'id': 3, 'name': 'Mike Johnson', 'age': 45, 'city': 'Chicago'},
        {'id': 4, 'name': 'Emily Davis', 'age': 22, 'city': 'London'},
    ]
    # Test empty data
    #data = []
    return render(request, 'render.html', {'data': data})
