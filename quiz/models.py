from django.db import models
from django.core import validators
from lessons.models import Theme

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=200,  blank=False, null=False, default='Вопрос', verbose_name='Вопрос', validators=[validators.MinLengthValidator(2)])
    var1 = models.CharField(max_length=200,  blank=True, null=True, verbose_name='Вариант 1')
    var2 = models.CharField(max_length=200,  blank=True, null=True, verbose_name='Вариант 2')
    var3 = models.CharField(max_length=200,  blank=True, null=True, verbose_name='Вариант 3')
    var4 = models.CharField(max_length=200,  blank=True, null=True, verbose_name='Вариант 4')
    answer = models.CharField(max_length=200,  blank=True, null=True, verbose_name='Правильный ответ', default='var', help_text='(!) Используй var1, var2, var3, var4 для правильного ответа', validators=[validators.MinLengthValidator(4)])
    theme = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='К какой теме относится тест')

    class Meta:
        verbose_name_plural = 'Вопросы тестов'
        verbose_name = 'Вопрос теста'
        ordering = ['id']

    def __str__(self):
        return self.question