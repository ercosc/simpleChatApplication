from django.shortcuts import render
from django.views.generic import CreateView
from .models import User


def IndexCreate(request):
    return render(request, 'chat/index.html')
#class IndexCreate(CreateView):
#    template_name = 'chat/index.html'
#    model = User
#    fields = ['name', 'room']


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
