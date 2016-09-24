from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Post
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def home_page(request):
	return render(request, 'blog/home_page.html', {})

def register(request):
	return render(request, 'blog/register.html', {})