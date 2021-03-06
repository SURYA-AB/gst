# Generated by Django 4.0 on 2022-01-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_task_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='clientname',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='time_from',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='time_to',
            field=models.TimeField(null=True),
        ),
    ]
