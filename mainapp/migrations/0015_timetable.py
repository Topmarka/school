# Generated by Django 3.2.7 on 2021-09-07 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20210907_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время урока')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.group', verbose_name='Группа')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Рассписание урока',
                'verbose_name_plural': 'Рассписание занятий',
            },
        ),
    ]
