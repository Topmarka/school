# Generated by Django 3.2.7 on 2021-10-24 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20211024_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название вакансии')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='Зарплата')),
                ('requirements', models.TextField(verbose_name='Требования к кандидату')),
                ('conditions', models.TextField(verbose_name='Условия работы')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата размещения вакансии')),
                ('active', models.BooleanField(default=True, verbose_name='Активная вакансия')),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='vacancy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.vacancy', verbose_name='Вакансия'),
        ),
    ]
