# Generated by Django 2.0.2 on 2018-06-16 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='autor',
            field=models.CharField(default=None, max_length=100, null=None),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='kategoria',
            field=models.CharField(default=None, max_length=100, null=None),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='tytul',
            field=models.CharField(default=None, max_length=100, null=None),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='wersja',
            field=models.CharField(default=None, max_length=100, null=None),
        ),
    ]