from django.shortcuts import render
from django.views.generic.edit import CreateView 
from .models import *


def board(request):

	context = {}
	messages = Message.objects.all()
	context['messages'] = messages
	comments = Comment.objects.all()
	context['comments'] = comments

	return render(request, "board.html", context)


