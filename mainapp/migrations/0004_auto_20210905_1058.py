# Generated by Django 3.2.7 on 2021-09-05 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210905_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название группы')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.profile')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.group', verbose_name='Группа')),
            ],
            bases=('mainapp.profile',),
        ),
    ]
