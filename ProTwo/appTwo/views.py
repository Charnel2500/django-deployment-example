from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
