# Generated by Django 3.2.7 on 2021-09-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210905_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_finished',
            field=models.ManyToManyField(blank=True, related_name='is_finished_course', to='mainapp.Student', verbose_name='Обучающиеся завершившие курс'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_finished',
            field=models.ManyToManyField(blank=True, related_name='is_finished_lesson', to='mainapp.Student', verbose_name='Обучающиеся завершившие урок'),
        ),
    ]
