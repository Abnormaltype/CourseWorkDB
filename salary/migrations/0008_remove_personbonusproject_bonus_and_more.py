# Generated by Django 4.0.2 on 2022-06-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0007_alter_person_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personbonusproject',
            name='bonus',
        ),
        migrations.AddField(
            model_name='personbonusproject',
            name='bonus',
            field=models.ManyToManyField(related_name='bonus', to='salary.Bonus'),
        ),
    ]
