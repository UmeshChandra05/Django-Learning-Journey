from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

def destination_detail(request, name):
    if request.user.is_authenticated:
        dest = get_object_or_404(Destination, name = name)
        return render(request, 'destination.html', {'dest': dest})
    else:
        messages.error(request, '⚠️ Please login to continue')
        return redirect("login")