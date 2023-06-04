from django.db import models
from django.core import validators

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Уроки по', help_text='Пиши в дательном падеже <br>С маленькой буквы', validators=[validators.MinLengthValidator(2)])
    serial = models.IntegerField(null=False, blank=False, verbose_name='Порядковый номер', default='1', unique=True, validators=[validators.MinValueValidator(0, message='Минимальное значение 0')])

    class Meta:
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name='Название урока', default='Название урока', help_text='С маленькой буквы', validators=[validators.MinLengthValidator(2)])
    text = models.TextField(null=False, blank=False, verbose_name='Урок', default='<p>Текст урока</p>', help_text=('Пиши используя HTML тэги, через них происходит конвертация стиля.<br> <_p><_/p> для обычного абзаца. <br> <_img src="/media/FILENAME.png"> для изображения. <br> <_ul><_li><_/li><_/li> для формата списка. <br> <_container-images><_/container-images> для создания контейнера с 2-я изображениями. <br> <_long-image-near-text> для 2-х изображений рядом с текстом. Внутри для изображений <_container-images-block><_img><_img><_/container-images-block>, а для текста обычный абзац <_p>'))
    serial = models.IntegerField(null=False, blank=False, verbose_name='Порядковый номер урока', default='1', validators=[validators.MinValueValidator(0, message='Минимальное значение 0')])
    publish = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации', editable=False)
    preview_image_url = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ссылка на превью в текстовом виде', default='<img src="static/preview_empty-tag.png">')
    theme = models.ForeignKey(Theme, null=True, blank=True,verbose_name='Уроки по', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'
        ordering = ['publish']

    def __str__(self):
        return self.name