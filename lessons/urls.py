from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LessonsView.as_view(), name='index'),
    path('lesson/<int:lesson_id>/', by_lesson, name='Lesson'),
    path('about/', AboutUsView.as_view(), name='AboutUs'),
    path('search_result/', SearchView.as_view(), name='Search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)