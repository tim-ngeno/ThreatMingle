from django.shortcuts import render
from hub.models import Room


def index_view(request):
    """
    Defines the index view for the hub model
    """
    return render(
        request, 'hub/index.html', {'rooms': Room.objects.all(),
                                    "title": "Chat"}
    )


def room_view(request, room_name):
    """
    Defines the room view for the hub model
    """
    chat_room, created = Room.objects.get_or_create(name=room_name)
    if request.user.is_authenticated:
        chat_room.join(request.user)
    return render(request, 'hub/room.html', {'room': chat_room, "title":
                                             chat_room})
