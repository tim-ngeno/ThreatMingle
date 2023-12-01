from django.shortcuts import render
import os

api_key = os.getenv('VIRUSTOTAL_API_KEY')


def home(request):
    """
    Renders the base html template for the project
    """
    return render(request, 'home/base.html', {'api_key': api_key})
