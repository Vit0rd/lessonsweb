from django.db.models.query import QuerySet
from django.shortcuts import *
from django.views.generic.base import *
from django.views.generic.list import *
from django.db.models import Q

from .models import *
from quiz import models

# Create your views here.
class LessonsView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.all()
        context['themes'] = Theme.objects.all()
        context['lessons_ordered_by_theme'] = Lesson.objects.all().order_by('theme_id')
        return context


def by_lesson(request, lesson_id):
    lessons = Lesson.objects.all()
    themes = Theme.objects.all()
    current_lesson = Lesson.objects.get(pk=lesson_id)
    current_theme = current_lesson.theme
    quiz_themes = Theme.objects.all()
    questions=models.Quiz.objects.all()
    next_lesson = Lesson.objects.filter((Q(theme=current_lesson.theme) & Q(serial__gt=current_lesson.serial)) | Q(theme__gt=current_lesson.theme)).order_by('theme').first()
    prev_lesson = Lesson.objects.exclude((Q(theme=current_lesson.theme) & Q(serial__gte=current_lesson.serial)) | Q(theme__gt=current_lesson.theme)).order_by('-theme').first()
    if next_lesson is None:
        next_lesson = current_lesson
    if prev_lesson is None:
        prev_lesson = current_lesson
        
    context = {'lessons': lessons, 'themes':themes, 'current_lesson':current_lesson, 'current_theme':current_theme, 'prev_lesson':prev_lesson, 'next_lesson':next_lesson, 'quiz_themes': quiz_themes, 'questions': questions}
    return render(request, 'lessons.html', context)


class AboutUsView(TemplateView):
    template_name = 'AboutUs.html'


class SearchView(ListView):
    model = Lesson
    template_name = 'search.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Lesson.objects.filter(Q(text__icontains=query) | Q(name__icontains=query)).order_by('theme_id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context