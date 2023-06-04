from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('quiz/', (include('quiz.urls'))),    
    path('', (include('lessons.urls'))),
]
