# Generated by Django 3.2.7 on 2021-10-29 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20211024_1104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': '01. Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Договор', 'verbose_name_plural': '02. Договоры'},
        ),
        migrations.AlterModelOptions(
            name='cost',
            options={'verbose_name': 'Затрата', 'verbose_name_plural': '08. Затраты'},
        ),
        migrations.AlterModelOptions(
            name='costcategory',
            options={'verbose_name': 'Категория затрат', 'verbose_name_plural': '07. Категории затрат'},
        ),
        migrations.AlterModelOptions(
            name='interview',
            options={'verbose_name': 'Собеседование', 'verbose_name_plural': '06. Собеседования'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': '03. Заказы'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': '04. Заявки'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': '05. Вакансии'},
        ),
    ]
