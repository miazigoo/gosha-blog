# Generated by Django 3.0.5 on 2020-04-12 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'managed': True, 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
