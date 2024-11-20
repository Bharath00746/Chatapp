from django.shortcuts import render
from .models import Room, Message

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room).order_by('-timestamp')[:50]
    
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
    })