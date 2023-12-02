from django.shortcuts import render
from hub.models import Room


def index_view(request):
    """
    Defines the index view for the hub model
    """
    return render(
        request, 'hub/index.html', {'rooms': Room.objects.all()}
    )


def room_view(request, room_name):
    """
    Defines the room view for the hub model
    """
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'hub/room.html', {'room': chat_room})
