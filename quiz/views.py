from django.db.models.query import QuerySet
from django.shortcuts import *

from .models import *
from lessons import models


# Create your views here.
def quiz(request, quiz_id):
    questions=Quiz.objects.all()
    quiz_themes = models.Theme.objects.get(pk=quiz_id)
    current_quiz_theme = quiz_themes.name
    if request.method == 'POST':
        print(request.POST)
        wrong=0
        correct=0
        total=0
        for q in questions:
            if q.theme.name == current_quiz_theme:
                total+=1
                print(request.POST.get(q.question))
                print(q.answer)
                print()
                if q.answer == request.POST.get(q.question):
                    correct+=1
                else:
                    wrong+=1
        percent = (correct/total)*100
        context = {
            'quiz_themes': quiz_themes, 
            'questions': questions, 
            'current_quiz_theme': current_quiz_theme, 

            'wrong': wrong, 
            'correct': correct, 
            'total': total, 
            'time': request.POST.get('timer'), 
            'percent': percent
            }
        return render(request, 'result.html', context)
    else:
        context = {'quiz_themes': quiz_themes, 'questions': questions, 'current_quiz_theme': current_quiz_theme,}
        return render(request, 'quiz.html', context)