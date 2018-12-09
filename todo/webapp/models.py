from django.db import models




class Task(models.Model):
    name = models.CharField(max_length=80, verbose_name='Задача')
    status = models.CharField(max_length=30, blank=True, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    due_date = models.DateTimeField(verbose_name='Выполнить к')

    def __str__(self):
        return '%s %s %s' % (self.pk, self.name, self.status)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

