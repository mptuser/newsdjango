from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User




class Tags(models.Model):
    tag_name = models.CharField(max_length=30, verbose_name="Название тэга")

    def get_absolute_url(self):
        return reverse("url_tag", kwargs={"tag_id": self.pk})
    
    def get_update_url(self):
        return reverse("url_tag_update", kwargs={"obj_id": self.pk})

    def get_delete_url(self):
        return reverse("url_tag_delete", kwargs={"obj_id": self.pk})
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tag_name


class Notes(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.TextField(verbose_name='Текст статьи')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    fk_tag = models.ManyToManyField(to=Tags, verbose_name="Тэги")

    def get_absolute_url(self):
        return reverse("url_detail", kwargs={"note_id": self.pk})

    def get_update_url(self):
        return reverse("url_note_update", kwargs={"obj_id": self.pk})

    def get_delete_url(self):
        return reverse("url_note_delete", kwargs={"obj_id": self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    fk_note = models.ForeignKey(to='Notes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        permissions = (("can_see_author", "Можно видеть автора комментария."),)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)

    
