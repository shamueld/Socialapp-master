# Generated by Django 3.0.5 on 2020-04-26 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
