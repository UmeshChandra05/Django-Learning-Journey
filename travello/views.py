from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    
    dest1 = Destination('Mumbai', 'The City That I Never Visited', 900, 'destination_1.jpg', False)
    dest2 = Destination('Hyderabad', 'The City I Was Borught Up', 800, 'destination_2.jpg', True)
    dest3 = Destination('Chennai', 'The City That I Once Visited', 700, 'destination_3.jpg', False)
    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests': dests})