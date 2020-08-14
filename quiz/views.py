from django.shortcuts import render
from .models import Quiz

# Create your views here.
def home(request):
    data = {}
    data['quizes'] = Quiz.objects.all()
    return render(request, 'quiz/index.html', data)