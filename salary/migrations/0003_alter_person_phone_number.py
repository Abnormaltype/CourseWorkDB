# Generated by Django 4.0.2 on 2022-06-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0002_remove_main_full_salary_personbonusproject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]