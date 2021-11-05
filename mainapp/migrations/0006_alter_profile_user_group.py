# Generated by Django 3.2.7 on 2021-11-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211102_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_group',
            field=models.CharField(choices=[('admin', 'Администратор'), ('manager', 'Менеджер учебного процесса'), ('sales_manager', 'Менеджер по продажам'), ('hr', 'HR менеджер'), ('teacher', 'Преподаватель'), ('student', 'Студент')], default='student', max_length=50, verbose_name='Группа пользователей'),
        ),
    ]
