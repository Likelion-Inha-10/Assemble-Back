# Generated by Django 4.0.6 on 2022-07-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_alter_todolist_is_end_alter_todolist_is_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
