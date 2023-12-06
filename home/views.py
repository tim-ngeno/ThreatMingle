from decouple import config
from django.shortcuts import render


api_key = config('VIRUSTOTAL_API_KEY')


def home(request):
    """
    Renders the base html template for the project
    """
    return render(request, 'home/base.html', {'api_key': api_key})
