from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import POST

# Create your views here.
def index(request):
	posts = POST.objects.all()
	return render(request,'index.html',{'posts':posts})

def post(request, slug):
	print(slug)
	return render_to_response('post.html',{
		'post':get_object_or_404(POST, slug=slug)
	})

def about(request):
	return render(request,'about.html',{})