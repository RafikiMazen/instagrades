# Generated by Django 2.2.7 on 2019-11-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade_name',
            field=models.CharField(default='default grade name', max_length=200),
        ),
    ]
