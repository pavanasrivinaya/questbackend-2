# Generated by Django 3.1.2 on 2020-11-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20201120_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=240),
        ),
    ]