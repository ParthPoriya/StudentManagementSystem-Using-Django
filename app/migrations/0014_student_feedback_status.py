# Generated by Django 5.1.2 on 2024-11-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_student_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
