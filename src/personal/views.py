from django.shortcuts import render
from personal.models import Question
# Create your views here.

def home_screen_view(request):
    context = {}
    # context['some_string'] =  "this is some string that I'm passing to the view"
    # context['some_number'] = 12345

    # list_of_value = []
    # list_of_value.append("first entry")
    # list_of_value.append("second entry")
    # list_of_value.append("third entry")
    # list_of_value.append("fourth entry")

    # context['list_of_value'] = list_of_value

    questions = Question.objects.all()
    context['questions'] = questions
    
    return render(request, "personal/home.html", context)
