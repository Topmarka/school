# Generated by Django 3.2.7 on 2021-10-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_client_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата собеседования'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='result',
            field=models.CharField(choices=[('new', 'Назначено'), ('contract', 'Заключен договор'), ('passed', 'Сдал'), ('not_pass', 'Не сдал'), ('course', 'Рекомендованы курсы')], max_length=50, verbose_name='Результат собеседования'),
        ),
    ]
